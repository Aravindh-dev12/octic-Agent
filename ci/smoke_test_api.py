"""Dependency-light production smoke test for the Octic API."""
import os,sys
os.environ["OCTIC_AI_AGENT_API_TOKEN"]="ci-test-token"
from octic_ai_agent import api_server
async def fake_run_message(message,agent_name="default",history=None):
    return {"message":message,"agent_name":agent_name,"history":history or []}
api_server._run_message=fake_run_message
client=api_server.app.test_client()
assert client.get("/health").status_code==200
assert client.post("/chat",json={"message":"hello"}).status_code==401
headers={"Authorization":"Bearer ci-test-token"}
response=client.post("/chat",json={"message":"hello","agent":"research"},headers=headers)
assert response.status_code==200,response.get_data(as_text=True)
body=response.get_json()
assert body["response"]["message"]=="hello" and body["agent"]=="research"
assert body["response"]["history"]==[{"role":"user","content":"Earlier question"},{"role":"assistant","content":"Earlier answer"}]
assert client.post("/chat",json={},headers=headers).status_code==400
assert client.post("/chat",json={"message":"hello","agent":"unknown"},headers=headers).status_code==400
print("Octic AI Agent production API smoke test: PASS")
