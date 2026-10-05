"""Production HTTP API for Octic AI Agent."""
from __future__ import annotations
import asyncio, os, secrets, sys
from pathlib import Path
from typing import Any
from flask import Flask, jsonify, request
from flask_cors import CORS
import praisonai
try:
    from praisonai import PraisonAI
except ImportError:
    PraisonAI = None

SERVICE_NAME = "octic-ai-agent-api"
HOST = os.environ.get("OCTIC_AI_AGENT_API_HOST", "127.0.0.1").strip()
PORT = int(os.environ.get("OCTIC_AI_AGENT_API_PORT", "8080"))
AUTH_ENABLED = os.environ.get("OCTIC_AI_AGENT_API_AUTH", "enabled").strip().lower() != "disabled"
AUTH_TOKEN = os.environ.get("OCTIC_AI_AGENT_API_TOKEN")
MAX_MESSAGE_LENGTH = int(os.environ.get("OCTIC_AI_AGENT_MAX_MESSAGE_LENGTH", "12000"))
AGENT_FILE = Path(os.environ.get("OCTIC_AI_AGENT_AGENT_FILE", str(Path(__file__).with_name("agents.yaml")))).expanduser().resolve()

if AUTH_ENABLED and not AUTH_TOKEN:
    if HOST not in {"127.0.0.1", "localhost", "::1"}:
        raise RuntimeError("OCTIC_AI_AGENT_API_TOKEN is required when binding to a non-localhost host.")
    AUTH_TOKEN = secrets.token_urlsafe(32)
    print(f"[{SERVICE_NAME}] generated local-development API token; set OCTIC_AI_AGENT_API_TOKEN for production.", file=sys.stderr, flush=True)

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 64 * 1024
origins = [x.strip() for x in os.environ.get("OCTIC_AI_AGENT_API_CORS_ORIGINS", "").split(",") if x.strip()]
if origins:
    CORS(app, origins=origins)

def _authorized() -> bool:
    if not AUTH_ENABLED:
        return True
    scheme, _, token = request.headers.get("Authorization", "").partition(" ")
    return scheme.lower() == "bearer" and bool(AUTH_TOKEN) and secrets.compare_digest(token, AUTH_TOKEN or "")

async def _run_message(message: str) -> Any:
    arun = getattr(praisonai, "arun", None)
    if arun is not None:
        return await arun(agent_file=str(AGENT_FILE), framework="praisonai", cli_config={"topic": message})
    if PraisonAI is None:
        raise RuntimeError("PraisonAI runtime is not installed")
    return await asyncio.to_thread(PraisonAI(agent_file=str(AGENT_FILE)).run)

@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": SERVICE_NAME})

@app.get("/ready")
def ready():
    if not AGENT_FILE.is_file():
        return jsonify({"status": "not_ready", "reason": "agent_file_missing"}), 503
    return jsonify({"status": "ready", "service": SERVICE_NAME})

@app.post("/chat")
def chat():
    if not _authorized():
        return jsonify({"error": "Unauthorized"}), 401
    data = request.get_json(silent=True)
    message = data.get("message") if isinstance(data, dict) else None
    if not isinstance(message, str) or not message.strip():
        return jsonify({"error": "message must be a non-empty string"}), 400
    if len(message) > MAX_MESSAGE_LENGTH:
        return jsonify({"error": f"message exceeds {MAX_MESSAGE_LENGTH} characters"}), 413
    if not AGENT_FILE.is_file():
        return jsonify({"error": "agent configuration is unavailable"}), 503
    try:
        result = asyncio.run(_run_message(message.strip()))
        return jsonify({"response": result, "status": "success"})
    except Exception:
        app.logger.exception("Agent execution failed")
        return jsonify({"error": "agent execution failed", "status": "error"}), 500

@app.get("/agents")
def list_agents():
    if not _authorized():
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"agents": ["default"], "agent_file": str(AGENT_FILE), "service": SERVICE_NAME})

@app.errorhandler(413)
def request_too_large(_error):
    return jsonify({"error": "request too large"}), 413

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=False)
