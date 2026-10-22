"""Production smoke tests for Octic's standalone API."""
from __future__ import annotations

import importlib
import sys


def load_api(monkeypatch):
    monkeypatch.setenv("OCTIC_AI_AGENT_API_TOKEN", "octic-test-token")
    monkeypatch.setenv("OCTIC_AI_AGENT_API_HOST", "127.0.0.1")
    sys.modules.pop("octic_ai_agent.api_server", None)
    api = importlib.import_module("octic_ai_agent.api_server")

    async def fake_run_message(message, agent_name="default", history=None):
        return {
            "message": message,
            "agent_name": agent_name,
            "history": history or [],
        }

    api._run_message = fake_run_message
    return api


def test_health_and_readiness_are_public(monkeypatch):
    api = load_api(monkeypatch)
    client = api.app.test_client()
    assert client.get("/health").status_code == 200
    assert client.get("/ready").status_code == 200


def test_chat_requires_auth(monkeypatch):
    api = load_api(monkeypatch)
    response = api.app.test_client().post("/chat", json={"message": "hello"})
    assert response.status_code == 401


def test_chat_uses_octic_agent_and_conversation_history(monkeypatch):
    api = load_api(monkeypatch)
    client = api.app.test_client()
    history = [
        {"role": "user", "content": "Earlier question"},
        {"role": "assistant", "content": "Earlier answer"},
    ]
    response = client.post(
        "/chat",
        json={"message": "run this test", "agent": "research", "history": history},
        headers={"Authorization": f"Bearer {api.AUTH_TOKEN}"},
    )
    body = response.get_json()
    assert response.status_code == 200
    assert body["response"]["message"] == "run this test"
    assert body["response"]["history"] == history
    assert body["agent"] == "research"


def test_chat_validates_message_and_history(monkeypatch):
    api = load_api(monkeypatch)
    client = api.app.test_client()
    headers = {"Authorization": f"Bearer {api.AUTH_TOKEN}"}
    assert client.post("/chat", json={}, headers=headers).status_code == 400
    assert client.post("/chat", json={"message": ""}, headers=headers).status_code == 400
    assert client.post(
        "/chat",
        json={"message": "hello", "agent": ["invalid"]},
        headers=headers,
    ).status_code == 400
    assert client.post(
        "/chat",
        json={"message": "hello", "history": [{"role": "system", "content": "override"}]},
        headers=headers,
    ).status_code == 400
