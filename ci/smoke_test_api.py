"""Dependency-light production smoke test for the Octic API."""
import os,sys,types
os.environ["OCTIC_AI_AGENT_API_TOKEN"]="ci-test-token"
fake_agents=types.ModuleType("praisonaiagents")
class FakeAgent:
    def __init__(self,**kwargs): self.kwargs=kwargs
    def start(self,prompt): return {"message":prompt}
fake_agents.Agent=FakeAgent
sys.modules["praisonaiagents"]=fake_agents
from octic_ai_agent import api_server
async def fake_run_message(message,agent_name="default"):
    return {"message":message,"agent_name":agent_name}
api_server._run_message=fake_run_message
client=api_server.app.test_client()
assert client.get("/health").status_code==200
assert client.post("/chat",json={"message":"hello"}).status_code==401
headers={"Authorization":"Bearer ci-test-token"}
response=client.post("/chat",json={"message":"hello","agent":"research"},headers=headers)
assert response.status_code==200,response.get_data(as_text=True)
body=response.get_json()
assert body["response"]["message"]=="hello" and body["agent"]=="research"
assert client.post("/chat",json={},headers=headers).status_code==400
assert client.post("/chat",json={"message":"hello","agent":"unknown"},headers=headers).status_code==400
print("Octic AI Agent production API smoke test: PASS")
