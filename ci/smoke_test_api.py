"""Dependency-light production smoke test for Octic AI Agent API."""
import os, sys, types
os.environ["OCTIC_AI_AGENT_API_TOKEN"] = "ci-test-token"
fake = types.ModuleType("praisonai")
class FakePraisonAI:
    def __init__(self, agent_file): self.agent_file = agent_file
    def run(self): return {"fallback": True}
async def arun(**kwargs):
    return {"message": kwargs["cli_config"]["topic"]}
fake.PraisonAI = FakePraisonAI
fake.arun = arun
sys.modules["praisonai"] = fake
from octic_ai_agent import api_server
client = api_server.app.test_client()
assert client.get("/health").status_code == 200
assert client.post("/chat", json={"message":"hello"}).status_code == 401
r = client.post("/chat", json={"message":"hello"}, headers={"Authorization":"Bearer ci-test-token"})
assert r.status_code == 200, r.get_data(as_text=True)
assert r.get_json()["response"]["message"] == "hello"
assert client.post("/chat", json={}, headers={"Authorization":"Bearer ci-test-token"}).status_code == 400
print("Octic AI Agent production API smoke test: PASS")
