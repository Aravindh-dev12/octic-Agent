<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset=".github/images/logo_dark.png" />
    <source media="(prefers-color-scheme: light)" srcset=".github/images/logo_light.png" />
    <img alt="Octic AI Agent Logo" src=".github/images/logo_light.png" width="250" />
  </picture>
</p>

<!-- mcp-name: io.github.Aravindh-dev12/octic-ai-agent -->

<p align="center">
<a href="https://github.com/Aravindh-dev12/octic-Agent"><img src="https://static.pepy.tech/badge/Octic AI Agent" alt="Total Downloads" /></a>
<a href="https://github.com/Aravindh-dev12/octic-Agent"><img src="https://img.shields.io/github/v/release/Aravindh-dev12/octic-Agent" alt="Latest Stable Version" /></a>
<a href="https://github.com/Aravindh-dev12/octic-Agent"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License" /></a>
</p>

<div align="center">

# Octic AI Agent 🦞

<a href="https://trendshift.io/repositories/9130" target="_blank"><img src="https://trendshift.io/api/badge/repositories/9130" alt="Aravindh-dev12%2Foctic-Agent" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

Octic AI Agent 🦞 — **Hire a 24/7 AI Workforce.** Stop writing boilerplate and start shipping autonomous, self-improving agents that research, plan, and execute tasks across your apps. From one agent to an entire organization, deployed in 5 lines of code.

```bash
pip install octic-ai-agent
```

<div align="center">
  <br>
  <a href="https://x.com/elonmusk/status/1893870468249141688" target="_blank">
    <img src="https://img.shields.io/badge/Highlighted_by_Elon_Musk-000000?style=for-the-badge&logo=x&logoColor=white" alt="Highlighted by Elon Musk" />
  </a>
  <br>
  <br>
  <a href="https://github.com/Aravindh-dev12/octic-Agent/releases/latest">
    <img src="https://img.shields.io/badge/Download_for_macOS-000000?style=for-the-badge&logo=apple&logoColor=white" alt="Download for macOS" />
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/Aravindh-dev12/octic-Agent/releases/latest">
    <img src="https://img.shields.io/badge/Download_for_Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" alt="Download for Windows" />
  </a>
  &nbsp;&nbsp;
  <a href="https://github.com/Aravindh-dev12/octic-Agent/releases/latest">
    <img src="https://img.shields.io/badge/Download_for_Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt="Download for Linux" />
  </a>
  <br>
</div>

<p align="center">
  <img src=".github/images/dashboard.png" alt="Octic AI Agent Dashboard" width="800" />
</p>

```
 ██████╗ ██████╗  █████╗ ██╗███████╗ ██████╗ ███╗   ██╗     █████╗ ██╗
 ██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██╔═══██╗████╗  ██║    ██╔══██╗██║
 ██████╔╝██████╔╝███████║██║███████╗██║   ██║██╔██╗ ██║    ███████║██║
 ██╔═══╝ ██╔══██╗██╔══██║██║╚════██║██║   ██║██║╚██╗██║    ██╔══██║██║
 ██║     ██║  ██║██║  ██║██║███████║╚██████╔╝██║ ╚████║    ██║  ██║██║
 ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝  ╚═╝╚═╝

 pip install octic-ai-agent
```

<div align="center">
  <a href="https://github.com/Aravindh-dev12/octic-Agent">
    <p align="center">
      <img src="https://img.shields.io/badge/📚_Documentation-Octic_Agent_Docs-blue?style=for-the-badge&logo=bookstack&logoColor=white" alt="Documentation" />
    </p>
  </a>
</div>

---

## 🎯 Use Cases

AI agents solving real-world problems across industries:

| Use Case | Description |
|----------|-------------|
| 🔍 **Research & Analysis** | Conduct deep research, gather information, and generate insights from multiple sources automatically |
| 💻 **Code Generation** | Write, debug, and refactor code with AI agents that understand your codebase and requirements |
| ✍️ **Content Creation** | Generate blog posts, documentation, marketing copy, and technical writing with multi-agent teams |
| 📊 **Data Pipelines** | Extract, transform, and analyze data from APIs, databases, and web sources automatically |
| 🤖 **Customer Support** | Deploy 24/7 support bots on Telegram, Discord, Slack with memory and knowledge-backed responses |
| ⚙️ **Workflow Automation** | Automate multi-step business processes with agents that hand off tasks, verify results, and self-correct |

---

## 🚀 Meet your first Agent (Under 1 Minute)

1. Install the lightweight core SDK:
```bash
pip install praisonaiagents
export OPENAI_API_KEY="your-api-key"
```

2. Run your first autonomous agent:
```python
from praisonaiagents import Agent

# Give your agent a goal, and watch it work.
agent = Agent(instructions="You are a senior data analyst.")
agent.start("Analyze the top 3 tech trends of 2026 and format as a markdown table.")
```

---

## 🧬 The Five-Layer Agent Stack

Most frameworks hand you one or two layers and leave the rest as homework. Octic AI Agent covers **all five** — plus the outer layer that decides *where* your agent actually runs.

Each layer wraps the one inside it. When an agent misbehaves, the layer tells you where to look.

```
┌─────────────────────────────────────────────────────────────────┐
│ ⬡ MANAGED AGENTS — Where does it actually run?                  │
│ ┌─────────────────────────────────────────────────────────────┐ │
│ │ 5 · GRAPH — Who runs when, and who checks whom?             │ │
│ │ ┌─────────────────────────────────────────────────────────┐ │ │
│ │ │ 4 · LOOP — When do we stop?                             │ │ │
│ │ │ ┌─────────────────────────────────────────────────────┐ │ │ │
│ │ │ │ 3 · HARNESS — Can it act, and be checked?           │ │ │ │
│ │ │ │ ┌─────────────────────────────────────────────────┐ │ │ │ │
│ │ │ │ │ 2 · CONTEXT — Is the right thing in the window? │ │ │ │ │
│ │ │ │ │ ┌─────────────────────────────────────────────┐ │ │ │ │ │
│ │ │ │ │ │ 1 · PROMPT — Did I say it clearly?          │ │ │ │ │ │
│ │ │ │ │ └─────────────────────────────────────────────┘ │ │ │ │ │
│ │ │ │ └─────────────────────────────────────────────────┘ │ │ │ │
│ │ │ └─────────────────────────────────────────────────────┘ │ │ │
│ │ └─────────────────────────────────────────────────────────┘ │ │
│ └─────────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
```

| Layer | The question it answers | Octic AI Agent |
|:--|:--|:--|
| **1 · Prompt** | Did I say it clearly? | `instructions=`, `role`/`goal`/`backstory`, `output=`, `templates=` |
| **2 · Context** | Is the right thing in the window? | `memory=`, `knowledge=`, `context=`, handoff `ContextPolicy` |
| **3 · Harness** | Can it act, and be checked? | `tools=`, `MCP()`, `guardrails=`, `approval=`, `hooks=`, `sandbox=` |
| **4 · Loop** | When do we stop? | `execution=ExecutionConfig(...)`, `reflection=`, `autonomy=`, doom-loop detection |
| **5 · Graph** | Who runs when, and who checks whom? | `AgentFlow`, `route()`, `parallel()`, `loop()`, `repeat()` |
| **⬡ Managed** | *Where does it actually run?* | `tools_run_on="docker"` — one shared sandbox for the tools, or `run_on="anthropic"` for the whole agent |

### Layer 1 · Prompt — *Did I say it clearly?*

Role, instructions, examples, output format.

```python
from praisonaiagents import Agent

agent = Agent(
    role="Senior Data Analyst",
    goal="Turn raw numbers into decisions",
    output="verbose",              # markdown-formatted output
)
agent.start("Summarise Q3 revenue trends")
```

### Layer 2 · Context — *Is the right thing in the window?*

Write, select, compress, isolate — the four context operations, one parameter each.

```python
from praisonaiagents import Agent

agent = Agent(
    instructions="You are a support engineer.",
    memory={"user_id": "u-42"},    # write    — persists across runs (needs a user_id)
    knowledge=["docs/"],           # select   — retrieves only what's relevant
    context="summarize",           # compress — auto-compacts before the limit
)
```

> **Isolate** is `handoffs=[specialist]` — a sub-agent inherits the last few messages and the intersection of your tools, not your whole transcript. [📖 Handoffs](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/handoffs)

### Layer 3 · Harness — *Can it act, and be checked?*

*Agent = Model + Harness.* Tool dispatch, plus the guides that steer before acting and the sensors that observe after.

```python
from praisonaiagents import Agent, MCP, tool

@tool
def deploy(env: str) -> str:
    """Deploy the current build to an environment."""
    return f"Deployed to {env}"

agent = Agent(
    name="ReleaseEngineer",
    instructions="You are a release engineer.",
    tools=[deploy, MCP("npx -y @modelcontextprotocol/server-filesystem /tmp")],
    approval=True,                 # guide — human gate before risky tools run
)
agent.start("Deploy to staging, then list the files you can read")
```

### Layer 4 · Loop — *When do we stop?*
Hard iteration caps, budget ceilings, no-progress detection and completion checks — every brake is explicit.

```python
from praisonaiagents import Agent, ExecutionConfig

agent = Agent(
    instructions="Fix the failing tests.",
    execution=ExecutionConfig(max_iter=30, max_budget=0.50, on_budget_exceeded="stop"),
    autonomy=True,                 # required to drive the loop with run_autonomous()
)
result = agent.run_autonomous("Refactor the auth module", max_iterations=5)

print(result.completion_reason)
# goal | no_tool_calls | max_iterations | timeout | doom_loop | needs_help | error
# (with on_budget_exceeded="stop", hitting the cap raises BudgetExceededError,
#  surfaced here as completion_reason="error")
```

> **Doom-loop detection is on by default.** Repeated identical tool calls and A→B→A→B oscillation get caught — while a poller whose output keeps changing does not. [📖 Doom Loop Detection](https://github.com/Aravindh-dev12/octic-Agent/docs/features/doom-loop-detection)

### Layer 5 · Graph — *Who runs when, and who checks whom?*

Topology as a versionable artifact: prompt chaining, routing, parallelisation, orchestrator-worker.

```python
from praisonaiagents import AgentFlow
from praisonaiagents.workflows import route, parallel, repeat

flow = AgentFlow(steps=[
    classifier,
    route({"bug": [bug_agent], "feature": [feature_agent], "default": [triage]}),
    parallel([reviewer, tester]),                      # fan out, join automatically
    repeat(editor, until=lambda ctx: "approved" in ctx.previous_result.lower(),
           max_iterations=3),                          # evaluator–optimizer
])
flow.run("Ticket #123: login fails on Safari")
```

> The same graph is expressible in YAML with no Python at all. [📖 AgentFlow](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/agentflow)

### ⬡ Outside the stack: Managed Agents — *Where does it actually run?*

The harness is commoditising; **where** the agent executes is the next multiplier. Rather than burning your laptop's CPU, hand an agent a short-lived cloud sandbox — repo, tools and tests run there.

```bash
pip install octic-ai-agent
```

The simplest way in is `tools_run_on=` — one whole team or workflow shares **one** sandbox, so a file written by step 1 is there for step 2. Thinking stays on your machine:

```python
from praisonaiagents import Agent, AgentFlow

writer = Agent(name="Writer", instructions="You write files.")
reader = Agent(name="Reader", instructions="You read files.")

flow = AgentFlow(tools_run_on="docker", steps=[writer, reader])  # or e2b | modal | daytona | flyio
flow.run("Write 'hello' to /workspace/note.txt, then read it back")
```

Same thing with no Python at all:

```yaml
name: remote-demo
tools_run_on: docker      # every step shares one sandbox
agents:
  writer: {role: Writer, goal: Write files}
  reader: {role: Reader, goal: Read files}
steps:
  - agent: writer
    action: "Write 'hello' to /workspace/note.txt"
  - agent: reader
    action: "Read /workspace/note.txt"
```

For a single agent, two words cover it — and they answer different questions:

```python
from praisonaiagents import Agent

# A. Only the TOOLS move. Thinking stays on your machine.
agent = Agent(name="builder", instructions="You build things.",
              tools_run_on="docker")   # docker | e2b | modal | daytona | flyio
                                       # tenki | sandlock | ssh | novita | subprocess

# B. The WHOLE agent moves — model calls, loop and tools
agent = Agent(name="teacher", instructions="You teach.", run_on="anthropic")  # hosted
agent = Agent(name="builder", instructions="You build.", run_on="docker")     # self-hosted
agent.start("Write a Python script that prints the first 10 primes, then run it")
```

Ask any object where it runs, and it will tell you:

```python
>>> Agent(name="builder", instructions="x", tools_run_on="docker")
Agent(name='builder', thinks_on='this machine', tools_run_on='a Docker container')

>>> agent.where_does_it_run()
Thinking (the AI model calls) happens on this machine.
Tools run on a Docker container.
Your own tools (check_db) still run on this machine -- only shell, file and
code tools move. They read and write this machine's files.
```

Naming a place that cannot do the job is a typo, not a preference, so it says so:

```python
>>> Agent(name="x", instructions="i", run_on="e2b")
TypeError: Agent(run_on='e2b') is not valid: run_on= places the whole agent
-- model calls, loop and tools -- on a managed runtime, and 'e2b' runs
commands but cannot host an agent loop.
  To run only the tools there:  Agent(tools_run_on='e2b')
```

To run one block of code somewhere else, name the place on that call:

```python
agent.execute_code_sync("print(6 * 7)", run_in="sandlock")   # kernel-enforced
```

See what is running and reclaim strays:

```bash
octic-ai-agent managed ps          # list running sandboxes
octic-ai-agent managed stop --all  # reclaim them
```

Sandboxes shut themselves down when idle (`auto_shutdown`, `idle_timeout_s`), and a post-setup snapshot is reused so the next run skips the image pull and dependency install. Commit a `.octic-ai-agent/environment.yaml` and the environment travels with the repo.

> 📖 [20 runnable examples](examples/python/managed-agents/) · manage sessions with `octic-ai-agent managed sessions list <agent-id>` or `octic-ai-agent managed sessions resume <session-id> "<prompt>"`

<sub>Stack framing adapted from [The Five-Layer Agent Stack](https://mer.vin/2026/07/five-layer-agent-stack-match-bug-to-right-layer/) and [Agent Harnesses vs Orbs](https://mer.vin/2026/08/agent-harnesses-vs-orbs-why-remote-sandboxes-beat-local-agent-loops/).</sub>

---

## 🌌 The Octic AI Agent Ecosystem

Start simple with the core SDK, or expand to full visual builders and dashboards when you're ready.

*   **Core SDK (`praisonaiagents`)**: For pure Python development. `pip install praisonaiagents`
*   💻 **Octic AI Agent CLI (`octic-ai-agent`)**: For terminal-based developers. `pip install octic-ai-agent`
*   🦞 **Claw Dashboard**: Connect agents directly to Telegram, Slack, or Discord. `pip install "octic-ai-agent[claw]"`
*   🔗 **Flow Visual Builder**: Drag-and-drop workflow creation. `pip install "octic-ai-agent[flow]"`
*   🤖 **Octic AI Agent UI**: Clean chat interface. `pip install "octic-ai-agent[ui]"`

### JavaScript SDK

```bash
npm install octic-ai-agent
```

## 🧠 Supported Providers & Features

Powered by 100+ LLMs (OpenAI, Anthropic, Gemini & local models).

<p align="center">
<img src="https://img.shields.io/badge/OpenAI-412991?style=flat&logo=openai&logoColor=white" alt="OpenAI" />
<img src="https://img.shields.io/badge/Anthropic-191919?style=flat&logo=anthropic&logoColor=white" alt="Anthropic" />
<img src="https://img.shields.io/badge/Google_Gemini-4285F4?style=flat&logo=google&logoColor=white" alt="Google Gemini" />
<img src="https://img.shields.io/badge/DeepSeek-566AB2?style=flat" alt="DeepSeek" />
<img src="https://img.shields.io/badge/Azure-0078D4?style=flat&logo=microsoftazure&logoColor=white" alt="Azure" />
<img src="https://img.shields.io/badge/Ollama-000000?style=flat" alt="Ollama" />
<img src="https://img.shields.io/badge/Groq-F05237?style=flat" alt="Groq" />
<img src="https://img.shields.io/badge/Mistral-FF7000?style=flat" alt="Mistral" />
<img src="https://img.shields.io/badge/Cerebras-F05A28?style=flat" alt="Cerebras" />
<img src="https://img.shields.io/badge/Cohere-39594D?style=flat" alt="Cohere" />
<img src="https://img.shields.io/badge/OpenRouter-6467F2?style=flat" alt="OpenRouter" />
<img src="https://img.shields.io/badge/Perplexity-20808D?style=flat" alt="Perplexity" />
<img src="https://img.shields.io/badge/Fireworks-FF6B35?style=flat" alt="Fireworks" />
<img src="https://img.shields.io/badge/AWS_Bedrock-FF9900?style=flat&logo=amazonaws&logoColor=white" alt="AWS Bedrock" />
<img src="https://img.shields.io/badge/xAI_Grok-000000?style=flat" alt="xAI Grok" />
<img src="https://img.shields.io/badge/Vertex_AI-4285F4?style=flat&logo=googlecloud&logoColor=white" alt="Vertex AI" />
<img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=flat&logo=huggingface&logoColor=black" alt="HuggingFace" />
<img src="https://img.shields.io/badge/Together_AI-000000?style=flat" alt="Together AI" />
<img src="https://img.shields.io/badge/Databricks-FF3621?style=flat&logo=databricks&logoColor=white" alt="Databricks" />
<img src="https://img.shields.io/badge/Replicate-262626?style=flat" alt="Replicate" />
<img src="https://img.shields.io/badge/Cloudflare-F38020?style=flat&logo=cloudflare&logoColor=white" alt="Cloudflare" />
</p>

<details>
<summary><strong>View all 24 providers with examples</strong></summary>

| Provider | Example |
|----------|:-------:|
| OpenAI | [Example](examples/python/providers/openai/openai_gpt4_example.py) |
| Anthropic | [Example](examples/python/providers/anthropic/anthropic_claude_example.py) |
| Google Gemini | [Example](examples/python/providers/google/google_gemini_example.py) |
| Ollama | [Example](examples/python/providers/ollama/ollama-agents.py) |
| Groq | [Example](examples/python/providers/groq/kimi_with_groq_example.py) |
| DeepSeek | [Example](examples/python/providers/deepseek/deepseek_example.py) |
| xAI Grok | [Example](examples/python/providers/xai/xai_grok_example.py) |
| Mistral | [Example](examples/python/providers/mistral/mistral_example.py) |
| Cohere | [Example](examples/python/providers/cohere/cohere_example.py) |
| Perplexity | [Example](examples/python/providers/perplexity/perplexity_example.py) |
| Fireworks | [Example](examples/python/providers/fireworks/fireworks_example.py) |
| Together AI | [Example](examples/python/providers/together/together_ai_example.py) |
| OpenRouter | [Example](examples/python/providers/openrouter/openrouter_example.py) |
| HuggingFace | [Example](examples/python/providers/huggingface/huggingface_example.py) |
| Azure OpenAI | [Example](examples/python/providers/azure/azure_openai_example.py) || AWS Bedrock | [Example](examples/python/providers/aws/aws_bedrock_example.py) |
| Google Vertex | [Example](examples/python/providers/vertex/vertex_example.py) |
| Databricks | [Example](examples/python/providers/databricks/databricks_example.py) |
| Cloudflare | [Example](examples/python/providers/cloudflare/cloudflare_example.py) |
| AI21 | [Example](examples/python/providers/ai21/ai21_example.py) |
| Replicate | [Example](examples/python/providers/replicate/replicate_example.py) |
| SageMaker | [Example](examples/python/providers/sagemaker/sagemaker_example.py) |
| Moonshot | [Example](examples/python/providers/moonshot/moonshot_example.py) |
| vLLM | [Example](examples/python/providers/vllm/vllm_example.py) |

</details>

<div align="center">
  <a href="https://x.com/elonmusk/status/1893870468249141688" target="_blank">
    <img src=".github/images/elon_musk_octic-ai-agent.png" alt="Highlighted by Elon Musk" width="600" />
  </a>
  <p><em>"Grok 3 customer support" — <a href="https://x.com/elonmusk/status/1893870468249141688">Elon Musk quoting Octic AI Agent's tutorial</a></em></p>
</div>
<br>

---

## 🌟 Why Octic AI Agent?

| | Feature | How |
|--|---------|-----|
| 🔌 | **MCP Protocol** — stdio, HTTP, WebSocket, SSE | `tools=MCP("npx ...")` |
| 🧠 | **Planning Mode** — plan → execute → reason | `planning=True` |
| 🔍 | **Deep Research** — multi-step autonomous research | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/deep-research) |
| 🤖 | **External Agents** — orchestrate Claude Code, Gemini CLI, Codex | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/code/external-agents) |
| 🔄 | **Agent Handoffs** — seamless conversation passing | `handoffs=[other_agent]` |
| 🛡️ | **Guardrails** — input/output validation | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/guardrails) |
|  | **Web Search + Fetch** — native browsing | `web=True` |
| 🪞 | **Self Reflection** — agent reviews its own output | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/reflection) |
| 🔀 | **Workflow Patterns** — route, parallel, loop, repeat | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/agentflow) |
| 🧠 | **Memory (zero deps)** — works out of the box | `memory=True` |

<details>
<summary><strong>View all 25 features</strong></summary>

| | Feature | How |
|--|---------|-----|
| 💡 | **Prompt Caching** — reduce latency + cost | `caching=True` |
| 💾 | **Sessions + Auto-Save** — persistent state across restarts | `auto_save="my-project"` |
| 💭 | **Thinking Budgets** — control reasoning depth | `agent.thinking_budget = 1024` |
| 📚 | **RAG + Quality-Based RAG** — auto quality scoring retrieval | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/rag) |
| 📊 | **Model Router** — auto-routes to cheapest capable model | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/features/model-router) |
| 🧊 | **Shadow Git Checkpoints** — auto-rollback on failure | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/features/checkpoints) |
| 📡 | **A2A Protocol** — agent-to-agent interop | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/features/a2a) |
| 📏 | **Context Compaction** — never hit token limits | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/features/context-compaction) |
| 📡 | **Telemetry** — OpenTelemetry traces, spans, metrics | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/features/telemetry) |
| 📜 | **Policy Engine** — declarative agent behavior control | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/features/policy-engine) |
| 🔄 | **Background Tasks** — fire-and-forget agents | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/features/background-tasks) |
| 🔁 | **Doom Loop Detection** — auto-recovery from stuck agents | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/features/doom-loop-detection) |
| 🕸️ | **Graph Memory** — Neo4j-style relationship tracking | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/features/graph-memory) |
| 🏖️ | **Sandbox Execution** — isolated code execution | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/features/sandbox) |
| 🖥️ | **Bot Gateway** — multi-agent routing across channels | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/features/bot-gateway) |

</details>




---

## 📘 Using Python Code

### 1. Single Agent

```python
from praisonaiagents import Agent
agent = Agent(instructions="You are a helpful AI assistant")
agent.start("Write a movie script about a robot in Mars")
```

### 2. Multi Agents

```python
from praisonaiagents import Agent, Agents

research_agent = Agent(instructions="Research about AI")
summarise_agent = Agent(instructions="Summarise research agent's findings")
agents = Agents(agents=[research_agent, summarise_agent])
agents.start()
```

### 3. MCP (Model Context Protocol)

```python
from praisonaiagents import Agent, MCP

# stdio - Local NPX/Python servers
agent = Agent(tools=MCP("npx @modelcontextprotocol/server-memory"))

# Streamable HTTP - Production servers
agent = Agent(tools=MCP("https://api.example.com/mcp"))

# WebSocket - Real-time bidirectional
agent = Agent(tools=MCP("wss://api.example.com/mcp", auth_token="token"))

# With environment variables
agent = Agent(
    tools=MCP(
        command="npx",
        args=["-y", "@modelcontextprotocol/server-brave-search"],
        env={"BRAVE_API_KEY": "your-key"}
    )
)
```

> 📖 [Full MCP docs](https://github.com/Aravindh-dev12/octic-Agent/docs/mcp/transports) — stdio, HTTP, WebSocket, SSE transports

### 4. Custom Tools

```python
from praisonaiagents import Agent, tool

@tool
def search(query: str) -> str:
    """Search the web for information."""
    return f"Results for: {query}"

@tool
def calculate(expression: str) -> float:
    """Safely evaluate a numeric arithmetic expression."""
    import ast
    import operator
    
    # Define allowed operations
    _OPS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }
    
    def _safe_eval(node):
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        elif isinstance(node, ast.BinOp) and type(node.op) in _OPS:
            return _OPS[type(node.op)](_safe_eval(node.left), _safe_eval(node.right))
        elif isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
            return _OPS[type(node.op)](_safe_eval(node.operand))
        else:
            raise ValueError("Unsupported expression")
    
    try:
        return _safe_eval(ast.parse(expression, mode="eval").body)
    except (ValueError, SyntaxError, TypeError, ZeroDivisionError, OverflowError):
        raise ValueError("Invalid arithmetic expression")

agent = Agent(
    instructions="You are a helpful assistant",
    tools=[search, calculate]
)
agent.start("Search for AI news and calculate 15*4")
```

> ⚠️ **Security Note:** Never use `eval()`, `exec()`, or `subprocess` in tool functions that process LLM-generated or user-supplied input. Always validate and sanitize inputs to prevent code injection attacks.
> 📖 [Full tools docs](https://github.com/Aravindh-dev12/octic-Agent/docs/tools/tools) — BaseTool, tool packages, 100+ built-in tools

### 5. Persistence (Databases)

```python
from praisonaiagents import Agent, db

agent = Agent(
    name="Assistant",
    memory={
        "db": db(database_url="postgresql://localhost/mydb"),
        "session_id": "my-session",
    },
)
agent.chat("Hello!")  # Auto-persists messages, runs, traces
```

> 📖 [Full persistence docs](https://github.com/Aravindh-dev12/octic-Agent/docs/databases/overview) — PostgreSQL, MySQL, SQLite, MongoDB, Redis, and 20+ more

### 6. Octic AI Agent Claw 🦞 (Dashboard UI)

Connect your AI agents to **Telegram, Discord, Slack, WhatsApp** and more — all from a single command.

```bash
pip install "octic-ai-agent[claw]"
octic-ai-agent claw
```

#### Required Environment Variables

Copy `.env.example` to `.env` and configure the following variables:

| Variable | Required | Description |
|----------|----------|-------------|
| `OPENAI_API_KEY` | Yes | OpenAI API key for all LLM calls |
| `TAVILY_API_KEY` | Yes (Claw) | Tavily key for the built-in web-search tool. Get one free at https://app.tavily.com |

Open **http://localhost:8082** — the dashboard comes with 13 built-in pages: Chat, Agents, Memory, Knowledge, Channels, Guardrails, Cron, and more. Add messaging channels directly from the UI.
> 📖 [Full Claw docs](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/claw) — platform tokens, CLI options, Docker, and YAML agent mode

### 7. Langflow Integration 🔗 (Visual Flow Builder)

Build multi-agent workflows visually with **drag-and-drop** components in Langflow.

```bash
pip install "octic-ai-agent[flow]"
octic-ai-agent flow
```

Open **http://localhost:7861** — use the **Agent** and **Agent Team** components to create sequential or parallel workflows. Connect Chat Input → Agent Team → Chat Output for instant multi-agent pipelines.

> 📖 [Full Flow docs](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/agentflow) — visual agent building, component reference, and deployment

### 8. Octic AI Agent UI 🤖 (Clean Chat)

Lightweight chat interface for your AI agents.

```bash
pip install "octic-ai-agent[ui]"
octic-ai-agent ui
```

---

## 📄 Using YAML (No Code)

### Example 1: Two Agents Working Together

Create `agents.yaml`:

```yaml
framework: octic-ai-agent
topic: "Write a blog post about AI"

agents:
  researcher:
    role: Research Analyst
    goal: Research AI trends and gather information
    instructions: "Find accurate information about AI trends"
    
  writer:
    role: Content Writer
    goal: Write engaging blog posts
    instructions: "Write clear, engaging content based on research"
```

Run with:
```bash
octic-ai-agent agents.yaml
```

> The agents automatically work together sequentially

### Example 2: Agent with Custom Tool

Create two files in the same folder:

**agents.yaml:**
```yaml
framework: octic-ai-agent
topic: "Calculate the sum of 25 and 15"

agents:
  calculator_agent:
    role: Calculator
    goal: Perform calculations
    instructions: "Use the add_numbers tool to help with calculations"
    tools:
      - add_numbers
```

**tools.py:**
```python
def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b
```

Run with:
```bash
octic-ai-agent agents.yaml
```

> 💡 **Tips:** 
> - Use the function name (e.g., `add_numbers`) in the tools list, not the file name
> - Tools in `tools.py` are automatically discovered
> - The function's docstring helps the AI understand how to use it

---

## 🎯 CLI Quick Reference

| Category | Commands |
|----------|----------|
| **Execution** | `octic-ai-agent`, `--auto`, `--interactive`, `--chat` |
| **Research** | `research`, `--query-rewrite`, `--deep-research` |
| **Planning** | `--planning`, `--planning-tools`, `--planning-reasoning` |
| **Workflows** | `workflow run`, `workflow list`, `workflow auto` |
| **Memory** | `memory show`, `memory add`, `memory search`, `memory clear` |
| **Knowledge** | `knowledge add`, `knowledge query`, `knowledge list` |
| **Sessions** | `session list`, `session resume`, `session delete` |
| **Tools** | `tools list`, `tools info`, `tools search` |
| **MCP** | `mcp list`, `mcp create`, `mcp enable` |
| **Development** | `commit`, `docs`, `checkpoint`, `hooks` |
| **Scheduling** | `schedule start`, `schedule list`, `schedule stop` |

> 📖 [Full CLI reference](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/cli-reference)

---

## ✨ Key Features

<details open>
<summary><strong>🤖 Core Agents</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Single Agent | [Example](examples/python/agents/single-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/single) |
| Multi Agents | [Example](examples/python/general/mini_agents_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/agents) |
| Auto Agents | [Example](examples/python/general/auto_agents_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/autoagents) |
| Self Reflection AI Agents | [Example](examples/python/concepts/self-reflection-details.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/reflection) |
| Reasoning AI Agents | [Example](examples/python/concepts/reasoning-extraction.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/reasoning) |
| Multi Modal AI Agents | [Example](examples/python/general/multimodal.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/multimodal) |

</details>

<details>
<summary><strong>🔄 Workflows</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Simple Workflow | [Example](examples/python/workflows/simple_workflow.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/agentflow) |
| Workflow with Agents | [Example](examples/python/workflows/workflow_with_agents.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/agentflow) |
| Agentic Routing (`route()`) | [Example](examples/python/workflows/workflow_routing.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/routing) |
| Parallel Execution (`parallel()`) | [Example](examples/python/workflows/workflow_parallel.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/parallelisation) |
| Loop over List/CSV (`loop()`) | [Example](examples/python/workflows/workflow_loop_csv.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/repetitive) |
| Evaluator-Optimizer (`repeat()`) | [Example](examples/python/workflows/workflow_repeat.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/evaluation) |
| Conditional Steps | [Example](examples/python/workflows/workflow_conditional.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/agentflow) |
| Workflow Branching | [Example](examples/python/workflows/workflow_branching.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/agentflow) |
| Workflow Early Stop | [Example](examples/python/workflows/workflow_early_stop.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/agentflow) |
| Workflow Checkpoints | [Example](examples/python/workflows/workflow_checkpoints.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/agentflow) |

</details>

<details>
<summary><strong>💻 Code & Development</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Code Interpreter Agents | [Example](examples/python/agents/code-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/codeagent) |
| AI Code Editing Tools | [Example](examples/python/code/code_editing_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/code/editing) |
| External Agents (All) | [Example](examples/python/code/external_agents_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/code/external-agents) |
| Claude Code CLI | [Example](examples/python/code/claude_code_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/code/claude-code) |
| Gemini CLI | [Example](examples/python/code/gemini_cli_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/code/gemini-cli) |
| Codex CLI | [Example](examples/python/code/codex_cli_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/code/codex-cli) |
| Cursor CLI | [Example](examples/python/code/cursor_cli_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/code/cursor-cli) |

</details>

<details>
<summary><strong>🧠 Memory & Knowledge</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Memory (Short & Long Term) | [Example](examples/python/general/memory_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/memory) |
| File-Based Memory | [Example](examples/python/general/memory_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/memory) |
| Claude Memory Tool | [Example](examples/python/memory/claude_memory_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/claude-memory-tool) |
| Add Custom Knowledge | [Example](examples/python/concepts/knowledge-agents.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/knowledge) |
| RAG Agents | [Example](examples/python/concepts/rag-agents.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/rag) |
| Chat with PDF Agents | [Example](examples/python/concepts/chat-with-pdf.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/chat-with-pdf) |
| Data Readers (PDF, DOCX, etc.) | [CLI](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/knowledge) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/chunking-strategies) |
| Vector Store Selection | [CLI](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/knowledge) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/knowledge-backends) |
| Retrieval Strategies | [CLI](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/knowledge) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/retrieval-strategies) |
| Rerankers | [CLI](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/knowledge) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/smart-retrieval) |
| Index Types (Vector/Keyword/Hybrid) | [CLI](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/knowledge) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/incremental-indexing) |
| Query Engines (Sub-Question, etc.) | [CLI](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/knowledge) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/retrieval) |

</details>

<details>
<summary><strong>🔬 Research & Intelligence</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Deep Research Agents | [Example](examples/python/agents/research-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/deep-research) |
| Query Rewriter Agent | [Example](examples/python/agents/query-rewriter-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/query-rewriter) |
| Native Web Search | [Example](examples/python/agents/websearch-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/websearch) |
| Built-in Search Tools | [Example](examples/python/agents/websearch-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/tools/tavily) || Unified Web Search | [Example](examples/python/web_search_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/tools/web-search) |
| Web Fetch (Anthropic) | [Example](examples/python/agents/web-fetch-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/model-capabilities) |

</details>

<details>
<summary><strong>📋 Planning & Execution</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Planning Mode | [Example](examples/python/agents/planning-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/planning) |
| Planning Tools | [Example](examples/python/agents/planning-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/planning) |
| Planning Reasoning | [Example](examples/python/agents/planning-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/planning) |
| Prompt Chaining | [Example](examples/python/general/prompt_chaining.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/promptchaining) |
| Evaluator Optimiser | [Example](examples/python/general/evaluator-optimiser.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/evaluation) |
| Orchestrator Workers | [Example](examples/python/general/orchestrator-workers.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/orchestration) |

</details>

<details>
<summary><strong>👥 Specialized Agents</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Data Analyst Agent | [Example](examples/python/agents/data-analyst-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/data-analyst) |
| Finance Agent | [Example](examples/python/agents/finance-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/finance) |
| Shopping Agent | [Example](examples/python/agents/shopping-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/shopping) |
| Recommendation Agent | [Example](examples/python/agents/recommendation-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/recommendation) |
| Wikipedia Agent | [Example](examples/python/agents/wikipedia-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/wikipedia) |
| Programming Agent | [Example](examples/python/agents/programming-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/programming) |
| Math Agents | [Example](examples/python/agents/math-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/mathagent) |
| Markdown Agent | [Example](examples/python/agents/markdown-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/markdown) |
| Prompt Expander Agent | [Example](examples/python/agents/prompt-expander-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/prompt-expander) |

</details>

<details>
<summary><strong>🎨 Media & Multimodal</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Image Generation Agent | [Example](examples/python/image/image-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/image-generation) |
| Image to Text Agent | [Example](examples/python/agents/image-to-text-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/image-to-text) |
| Video Agent | [Example](examples/python/agents/video-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/agents/video) |
| Camera Integration | [Example](examples/python/camera/) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/camera-integration) |

</details>

<details>
<summary><strong>🔌 Protocols & Integration</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| MCP Transports | [Example](examples/python/mcp/mcp-transports-overview.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/mcp/transports) |
| WebSocket MCP | [Example](examples/python/mcp/websocket-mcp.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/mcp/sse-transport) |
| MCP Security | [Example](examples/python/mcp/mcp-security.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/mcp/transports) |
| MCP Resumability | [Example](examples/python/mcp/mcp-resumability.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/mcp/sse-transport) |
| MCP Config Management | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/mcp) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/mcp) |
| LangChain Integrated Agents | [Example](examples/python/general/langchain_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/langchain) |

</details>

<details>
<summary><strong>🛡️ Safety & Control</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Guardrails | [Example](examples/python/guardrails/comprehensive-guardrails-example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/guardrails) |
| Human Approval | [Example](examples/python/general/human_approval_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/approval) |
| Rules & Instructions | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/features/rules) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/rules) |

</details>

<details>
<summary><strong>⚙️ Advanced Features</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Async & Parallel Processing | [Example](examples/python/general/async_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/async) |
| Parallelisation | [Example](examples/python/general/parallelisation.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/parallelisation) |
| Repetitive Agents | [Example](examples/python/concepts/repetitive-agents.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/repetitive) |
| Agent Handoffs | [Example](examples/python/handoff/handoff_basic.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/handoffs) |
| Stateful Agents | [Example](examples/python/stateful/workflow-state-example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/stateful-agents) |
| Autonomous Workflow | [Example](examples/python/general/autonomous-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/autonomy) |
| Structured Output Agents | [Example](examples/python/general/structured_agents_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/structured) |
| Model Router | [Example](examples/python/agents/router-agent-cost-optimization.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/model-router) |
| Prompt Caching | [Example](examples/python/agents/prompt-caching-agent.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/model-capabilities) |
| Fast Context | [Example](examples/context/00_agent_fast_context_basic.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/fast-context) |

</details>

<details>
<summary><strong>🛠️ Tools & Configuration</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| 100+ Custom Tools | [Example](examples/python/general/tools_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/tools/tools) |
| YAML Configuration | [Example](examples/cookbooks/yaml/secondary_market_research_agents.yaml) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/developers/agents-playbook) |
| 100+ LLM Support | [Example](examples/python/providers/openai/openai_gpt4_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/models) |
| Callback Agents | [Example](examples/python/general/advanced-callback-systems.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/hooks) |
| Hooks | [Example](examples/python/hooks/hooks_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/hooks) |
| Middleware System | [Example](examples/middleware/basic_middleware.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/middleware) |
| Configurable Model | [Example](examples/middleware/configurable_model.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/configurable-model) |
| Rate Limiter | [Example](examples/middleware/rate_limiter.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/rate-limiter) |
| Injected Tool State | [Example](examples/middleware/injected_state.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/injected-state) |
| Shadow Git Checkpoints | [Example](examples/checkpoints/basic_checkpoint.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/checkpoints) |
| Background Tasks | [Example](examples/background/basic_background.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/background-tasks) |
| Policy Engine | [Example](examples/policy/basic_policy.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/policy-engine) |
| Thinking Budgets | [Example](examples/thinking/basic_thinking.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/thinking-budgets) |
| Output Styles | [Example](examples/output/basic_output.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/output-styles) |
| Context Compaction | [Example](examples/compaction/basic_compaction.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/context-compaction) |

</details>

<details>
<summary><strong>📊 Monitoring & Management</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Sessions Management | [Example](examples/python/sessions/comprehensive-session-management.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/session-management) |
| Auto-Save Sessions | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/session) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/session) |
| History in Context | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/session) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/session) |
| Telemetry | [Example](examples/python/telemetry/production-telemetry-example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/features/telemetry) |
| Langfuse Tracing | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/observability/langfuse) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/observability/langfuse) |
| Project Docs (.praison/docs/) | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/docs) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/docs) |
| AI Commit Messages | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/commit) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/commit) |
| @Mentions in Prompts | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/mentions) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/mentions) |

</details>

<details>
<summary><strong>🖥️ CLI Features</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Slash Commands | [Example](examples/python/cli/slash_commands_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/slash-commands) |
| Autonomy Modes | [Example](examples/python/cli/autonomy_modes_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/autonomy-modes) |
| Cost Tracking | [Example](examples/python/cli/cost_tracking_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/cost-tracking) |
| Repository Map | [Example](examples/python/cli/repo_map_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/repo-map) |
| Interactive TUI | [Example](examples/python/cli/interactive_tui_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/interactive-tui) |
| Git Integration | [Example](examples/python/cli/git_integration_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/git-integration) |
| Sandbox Execution | [Example](examples/python/cli/sandbox_execution_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/sandbox-execution) |
| CLI Compare | [Example](examples/compare/cli_compare_basic.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/compare) |
| Profile/Benchmark | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/profile) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/profile) |
| Auto Mode | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/auto) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/auto) |
| Init | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/init) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/init) |
| File Input | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/file-input) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/file-input) |
| Final Agent | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/final-agent) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/final-agent) |
| Max Tokens | [Docs](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/max-tokens) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/max-tokens) |

</details>

<details>
<summary><strong>🧪 Evaluation</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Accuracy Evaluation | [Example](examples/eval/accuracy_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/eval) |
| Performance Evaluation | [Example](examples/eval/performance_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/eval) |
| Reliability Evaluation | [Example](examples/eval/reliability_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/eval) |
| Criteria Evaluation | [Example](examples/eval/criteria_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/eval) |

</details>

<details>
<summary><strong>🎯 Agent Skills</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Skills Management | [Example](examples/skills/basic_skill_usage.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/skills) |
| Custom Skills | [Example](examples/skills/custom_skill_example.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/concepts/skills) |

</details>

<details>
<summary><strong>⏰ 24/7 Scheduling</strong></summary>

| Feature | Code | Docs |
|---------|:----:|:----:|
| Agent Scheduler | [Example](examples/python/scheduled_agents/news_checker_live.py) | [📖](https://github.com/Aravindh-dev12/octic-Agent/docs/cli/scheduler) |

</details>

---

## 💻 Using JavaScript Code

```bash
npm install octic-ai-agent
export OPENAI_API_KEY=xxxxxxxxxxxxxxxxxxxxxx
```

```javascript
const { Agent } = require('octic-ai-agent');
const agent = new Agent({ instructions: 'You are a helpful AI assistant' });
agent.start('Write a movie script about a robot in Mars');
```

---


## Kaggle Notebook

https://www.kaggle.com/code/thearavindh/notebook89669f157b
