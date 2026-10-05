"""Octic AI Agent interactive web UI."""
from __future__ import annotations
import os, sys
from pathlib import Path
from typing import Any
import gradio as gr
ROOT=Path(__file__).resolve().parents[1]
PKG=ROOT/"src"/"octic_ai_agent"
if str(PKG) not in sys.path: sys.path.insert(0,str(PKG))
from octic_ai_agent import OcticAgent
AGENTS={
 "General Assistant":"You are Octic Assistant, a precise and helpful general-purpose AI agent.",
 "Research Analyst":"You are Octic Research Analyst. Separate facts from assumptions and use an evidence-driven process.",
 "Software Engineer":"You are Octic Software Engineer. Diagnose problems systematically and return maintainable implementation guidance.",
 "Data Analyst":"You are Octic Data Analyst. Analyze structured information carefully and state assumptions.",
 "Workflow Operator":"You are Octic Workflow Operator. Plan multi-step tasks, verify important results, and report blockers instead of guessing.",
}
def respond(message: str, history: list[dict[str,Any]]|None, agent_name: str, model: str):
 history=list(history or [])
 if not message or not message.strip(): return history,""
 if model.strip(): os.environ["OCTIC_AI_AGENT_MODEL"]=model.strip()
 else: os.environ.pop("OCTIC_AI_AGENT_MODEL",None)
 try:
  result=OcticAgent(AGENTS[agent_name],name=agent_name.replace(" ","")).start(message.strip())
  answer=str(result)
 except Exception as exc:
  answer=f"Execution failed: {type(exc).__name__}. Check provider credentials and runtime configuration."
 history += [{"role":"user","content":message.strip()},{"role":"assistant","content":answer}]
 return history,""
with gr.Blocks(title="Octic AI Agent") as demo:
 gr.Markdown("# ⬡ Octic AI Agent\nProduction-oriented agent workspace.")
 with gr.Row():
  agent=gr.Dropdown(list(AGENTS),value="General Assistant",label="Agent")
  model=gr.Textbox(value=os.environ.get("OCTIC_AI_AGENT_MODEL",""),label="Model (optional)")
 chat=gr.Chatbot(type="messages",height=520,label="Conversation")
 prompt=gr.Textbox(lines=4,label="Task",placeholder="Give the selected agent a concrete task…")
 with gr.Row():
  run=gr.Button("Run Agent",variant="primary")
  clear=gr.Button("Clear")
 run.click(respond,[prompt,chat,agent,model],[chat,prompt])
 prompt.submit(respond,[prompt,chat,agent,model],[chat,prompt])
 clear.click(lambda:([],""),outputs=[chat,prompt])
 gr.Markdown("GitHub UI: ui/app.py • Hugging Face Space: huggingface_space/ • Kaggle notebooks: kaggle/")
if __name__=="__main__":
 demo.launch(server_name=os.environ.get("GRADIO_SERVER_NAME","127.0.0.1"),server_port=int(os.environ.get("GRADIO_SERVER_PORT","7860")),show_error=False)