"""Hugging Face Space entrypoint for Octic AI Agent."""
import os
import gradio as gr
from octic_ai_agent import OcticAgent
AGENTS={
 "General Assistant":"You are Octic Assistant, precise and helpful.",
 "Research Analyst":"You are Octic Research Analyst. Separate facts from assumptions and use an evidence-driven process.",
 "Software Engineer":"You are Octic Software Engineer. Diagnose problems systematically and provide maintainable solutions.",
 "Data Analyst":"You are Octic Data Analyst. Analyze structured information carefully and state assumptions.",
 "Workflow Operator":"You are Octic Workflow Operator. Plan multi-step tasks, verify important results, and report blockers.",
}
def run_agent(message,agent_name,model):
 if not message or not message.strip(): return "Please enter a task."
 if model.strip(): os.environ["OCTIC_AI_AGENT_MODEL"]=model.strip()
 try: return str(OcticAgent(AGENTS[agent_name],name=agent_name.replace(" ","")).start(message.strip()))
 except Exception as exc: return f"Execution failed: {type(exc).__name__}. Check Space secrets and provider configuration."
with gr.Blocks(title="Octic AI Agent") as demo:
 gr.Markdown("# ⬡ Octic AI Agent\nInteractive production-oriented agent workspace.")
 agent=gr.Dropdown(list(AGENTS),value="General Assistant",label="Agent")
 model=gr.Textbox(value=os.environ.get("OCTIC_AI_AGENT_MODEL",""),label="Model (optional)")
 prompt=gr.Textbox(lines=5,label="Task",placeholder="Give the agent a concrete task…")
 output=gr.Markdown()
 run=gr.Button("Run Agent",variant="primary")
 run.click(run_agent,[prompt,agent,model],output)
 prompt.submit(run_agent,[prompt,agent,model],output)
if __name__=="__main__":
 demo.launch(server_name="0.0.0.0",server_port=int(os.environ.get("PORT","7860")))