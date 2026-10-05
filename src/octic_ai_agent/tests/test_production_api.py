"""Production smoke tests for the Octic API server."""
from __future__ import annotations
import importlib, sys, types
def load_api(monkeypatch):
    fake = types.ModuleType("praisonai")
    class FakePraisonAI:
        def __init__(self, agent_file): self.agent_file = agent_file
        def run(self): return {"fallback": True, "agent_file": self.agent_file}
    async def arun(**kwargs):
        return {"message": kwargs["cli_config"]["topic"], "agent_file": kwargs["agent_file"]}
    fake.PraisonAI = FakePraisonAI; fake.arun = arun
    monkeypatch.setitem(sys.modules, "praisonai", fake)
    sys.modules.pop("octic_ai_agent.api_server", None)
    return importlib.import_module("octic_ai_agent.api_server")
def test_health_is_public(monkeypatch):
    api = load_api(monkeypatch); assert api.app.test_client().get("/health").status_code == 200
def test_chat_requires_auth(monkeypatch):
    api = load_api(monkeypatch); assert api.app.test_client().post("/chat", json={"message":"hello"}).status_code == 401
def test_chat_uses_message(monkeypatch):
    api = load_api(monkeypatch); client = api.app.test_client()
    r = client.post("/chat", json={"message":"run this test"}, headers={"Authorization":f"Bearer {api.AUTH_TOKEN}"})
    assert r.status_code == 200 and r.get_json()["response"]["message"] == "run this test"
def test_chat_validates_message(monkeypatch):
    api = load_api(monkeypatch); client = api.app.test_client(); h={"Authorization":f"Bearer {api.AUTH_TOKEN}"}
    assert client.post("/chat", json={}, headers=h).status_code == 400
    assert client.post("/chat", json={"message":""}, headers=h).status_code == 400
