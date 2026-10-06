'use client';

import { FormEvent, KeyboardEvent, useEffect, useMemo, useState } from "react";
import {
  Activity,
  Bot,
  Check,
  ChevronDown,
  Circle,
  Command,
  Cpu,
  Database,
  Loader2,
  Menu,
  MessageSquare,
  PanelLeft,
  Plus,
  RefreshCw,
  Send,
  Settings2,
  ShieldCheck,
  Sparkles,
  TerminalSquare,
  Trash2,
  X,
  Zap,
} from "lucide-react";

type AgentKey = "default" | "research" | "developer" | "data" | "workflow";
type Message = {
  id: string;
  role: "user" | "agent" | "system";
  content: string;
  time: string;
};

type SystemState = "unknown" | "checking" | "online" | "offline";

const AGENTS: Record<
  AgentKey,
  { label: string; short: string; description: string; glyph: string }
> = {
  default: {
    label: "Octic General",
    short: "GENERAL",
    description: "General-purpose reasoning and task execution.",
    glyph: "O",
  },
  research: {
    label: "Research Analyst",
    short: "RESEARCH",
    description: "Evidence-driven analysis and structured synthesis.",
    glyph: "R",
  },
  developer: {
    label: "Software Engineer",
    short: "DEVELOPER",
    description: "Systematic debugging, implementation and code review.",
    glyph: "D",
  },
  data: {
    label: "Data Analyst",
    short: "DATA",
    description: "Structured analysis with explicit assumptions.",
    glyph: "A",
  },
  workflow: {
    label: "Workflow Operator",
    short: "WORKFLOW",
    description: "Plans multi-step work and verifies important outcomes.",
    glyph: "W",
  },
};

const STORAGE_KEY = "octic-agent-desktop:v1";

function nowLabel() {
  return new Intl.DateTimeFormat(undefined, {
    hour: "2-digit",
    minute: "2-digit",
  }).format(new Date());
}

function safeLoad(): Message[] {
  if (typeof window === "undefined") return [];
  try {
    const raw = window.localStorage.getItem(STORAGE_KEY);
    const parsed = raw ? JSON.parse(raw) : [];
    return Array.isArray(parsed) ? parsed : [];
  } catch {
    return [];
  }
}

export default function Page() {
  const [agent, setAgent] = useState<AgentKey>("default");
  const [messages, setMessages] = useState<Message[]>(safeLoad);
  const [input, setInput] = useState("");
  const [sending, setSending] = useState(false);
  const [system, setSystem] = useState<SystemState>("unknown");
  const [mobileNav, setMobileNav] = useState(false);
  const [showSettings, setShowSettings] = useState(false);
  const [lastError, setLastError] = useState("");
  const [backendUpdated, setBackendUpdated] = useState("");

  const current = AGENTS[agent];

  useEffect(() => {
    window.localStorage.setItem(STORAGE_KEY, JSON.stringify(messages));
  }, [messages]);

  const sessionMessages = useMemo(() => messages.filter((m) => m.role !== "system"), [messages]);

  async function checkSystem() {
    setSystem("checking");
    try {
      const [healthRes, readyRes] = await Promise.all([
        fetch("/api/agent?action=health", { cache: "no-store" }),
        fetch("/api/agent?action=ready", { cache: "no-store" }),
      ]);
      setSystem(healthRes.ok && readyRes.ok ? "online" : "offline");
      setBackendUpdated(nowLabel());
      setLastError("");
    } catch {
      setSystem("offline");
      setLastError("The Vercel app could not reach its agent backend.");
    }
  }

  useEffect(() => {
    checkSystem();
    const id = window.setInterval(checkSystem, 30_000);
    return () => window.clearInterval(id);
  }, []);

  function resetSession() {
    setMessages([]);
    setInput("");
    setLastError("");
  }

  async function sendMessage(event?: FormEvent) {
    event?.preventDefault();
    const message = input.trim();
    if (!message || sending) return;

    const userMessage: Message = {
      id: crypto.randomUUID(),
      role: "user",
      content: message,
      time: nowLabel(),
    };
    setMessages((items) => [...items, userMessage]);
    setInput("");
    setSending(true);
    setLastError("");

    try {
      const response = await fetch("/api/agent", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({ message, agent }),
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) {
        throw new Error(typeof data?.error === "string" ? data.error : "Agent execution failed.");
      }

      const rendered =
        typeof data?.response === "string"
          ? data.response
          : JSON.stringify(data?.response ?? data, null, 2);

      setMessages((items) => [
        ...items,
        {
          id: crypto.randomUUID(),
          role: "agent",
          content: rendered,
          time: nowLabel(),
        },
      ]);
      await checkSystem();
    } catch (error) {
      const text = error instanceof Error ? error.message : "Agent execution failed.";
      setLastError(text);
    } finally {
      setSending(false);
    }
  }

  function handleKeyDown(event: KeyboardEvent<HTMLTextAreaElement>) {
    if (event.key === "Enter" && !event.shiftKey) {
      event.preventDefault();
      void sendMessage();
    }
  }

  return (
    <main className="shell">
      <aside className={`sidebar ${mobileNav ? "sidebar-open" : ""}`}>
        <div className="brand-row">
          <div className="brand-mark">⬡</div>
          <div>
            <div className="brand">OCTIC</div>
            <div className="brand-sub">AI AGENT DESKTOP</div>
          </div>
          <button className="icon-button mobile-close" onClick={() => setMobileNav(false)} aria-label="Close navigation">
            <X size={17} />
          </button>
        </div>

        <div className="sidebar-section">
          <div className="section-label">WORKSPACE</div>
          <button className="workspace-button">
            <span className="workspace-icon"><PanelLeft size={15} /></span>
            <span className="workspace-copy">
              <strong>Primary Workspace</strong>
              <small>Local project context</small>
            </span>
            <ChevronDown size={14} />
          </button>
        </div>

        <div className="sidebar-section">
          <div className="section-label">BUILT-IN AGENTS</div>
          <div className="agent-list">
            {(Object.entries(AGENTS) as [AgentKey, typeof AGENTS[AgentKey]][]).map(([key, value]) => (
              <button
                key={key}
                className={`agent-row ${agent === key ? "selected" : ""}`}
                onClick={() => {
                  setAgent(key);
                  setMobileNav(false);
                }}
              >
                <span className="agent-glyph">{value.glyph}</span>
                <span className="agent-copy">
                  <strong>{value.label}</strong>
                  <small>{value.short}</small>
                </span>
                {agent === key && <Check size={15} />}
              </button>
            ))}
          </div>
        </div>

        <div className="sidebar-section compact">
          <div className="section-label">TOOLS</div>
          <button className="utility-row"><TerminalSquare size={16} /><span>Command workspace</span></button>
          <button className="utility-row"><Database size={16} /><span>Memory & context</span></button>
          <button className="utility-row"><ShieldCheck size={16} /><span>Execution safety</span></button>
        </div>

        <div className="sidebar-footer">
          <div className={`connection-pill ${system}`}>
            <span className="status-dot" />
            <span>{system === "online" ? "RUNTIME ONLINE" : system === "checking" ? "CHECKING RUNTIME" : system === "offline" ? "RUNTIME OFFLINE" : "RUNTIME UNKNOWN"}</span>
          </div>
          <button className="utility-row" onClick={() => setShowSettings(true)}>
            <Settings2 size={16} /><span>Settings</span>
          </button>
        </div>
      </aside>

      {mobileNav && <button className="backdrop" onClick={() => setMobileNav(false)} aria-label="Close navigation" />}

      <section className="workspace">
        <header className="topbar">
          <div className="topbar-left">
            <button className="icon-button menu-trigger" onClick={() => setMobileNav(true)} aria-label="Open navigation">
              <Menu size={18} />
            </button>
            <div className="route"><span>OCTIC</span><span className="route-sep">/</span><strong>AGENT</strong></div>
            <div className="desktop-chip"><Command size={12} /> DESKTOP</div>
          </div>
          <div className="topbar-right">
            <div className={`status-inline ${system}`}><span className="status-dot" />{system === "online" ? "Connected" : "Backend unavailable"}</div>
            <button className="icon-button" onClick={checkSystem} aria-label="Refresh connection">
              <RefreshCw size={16} className={system === "checking" ? "spin" : ""} />
            </button>
            <button className="top-new" onClick={resetSession}><Plus size={15} /> New run</button>
          </div>
        </header>

        <div className="content-grid">
          <div className="conversation-panel">
            <div className="hero-strip">
              <div>
                <div className="eyebrow">AUTONOMOUS AGENT CONSOLE</div>
                <h1>{current.label}</h1>
                <p>{current.description}</p>
              </div>
              <div className="agent-chip">
                <span className="chip-glyph">{current.glyph}</span>
                <span>{current.short}</span>
              </div>
            </div>

            {sessionMessages.length === 0 ? (
              <div className="empty-state">
                <div className="empty-mark"><Sparkles size={20} /></div>
                <div className="empty-title">Ready for a task.</div>
                <div className="empty-copy">Send a goal, question or implementation task. Octic will run it through the selected agent profile.</div>
                <div className="suggestions">
                  {[
                    "Investigate a failing deployment and summarize the likely root cause.",
                    "Design a production-ready REST API for a multi-tenant agent service.",
                    "Analyze a dataset and explain the three highest-impact anomalies.",
                  ].map((text) => (
                    <button key={text} className="suggestion" onClick={() => setInput(text)}>{text}<Zap size={14} /></button>
                  ))}
                </div>
              </div>
            ) : (
              <div className="message-stream">
                {sessionMessages.map((message) => (
                  <article key={message.id} className={`message-card ${message.role}`}>
                    <div className="message-meta">
                      <span className="message-role">{message.role === "user" ? "YOU" : "OCTIC"}</span>
                      <span>{message.time}</span>
                    </div>
                    <div className="message-content">{message.content}</div>
                  </article>
                ))}
                {sending && (
                  <article className="message-card agent pending">
                    <div className="message-meta"><span className="message-role">OCTIC</span><span>RUNNING</span></div>
                    <div className="running"><Loader2 size={16} className="spin" /> Agent is executing the task…</div>
                  </article>
                )}
              </div>
            )}

            <div className="composer-wrap">
              {lastError && <div className="error-banner">{lastError}</div>}
              <form className="composer" onSubmit={sendMessage}>
                <div className="composer-head">
                  <span className="composer-tag"><Circle size={8} fill="currentColor" /> {current.short}</span>
                  <span className="composer-hint">ENTER TO RUN · SHIFT+ENTER FOR NEW LINE</span>
                </div>
                <textarea
                  value={input}
                  onChange={(event) => setInput(event.target.value)}
                  onKeyDown={handleKeyDown}
                  placeholder="Describe what you want the agent to do…"
                  rows={4}
                  maxLength={12_000}
                  disabled={sending}
                />
                <div className="composer-foot">
                  <span>{input.length.toLocaleString()} / 12,000</span>
                  <div className="composer-actions">
                    <button type="button" className="icon-button" onClick={() => setInput("")} aria-label="Clear input"><Trash2 size={15} /></button>
                    <button type="submit" className="run-button" disabled={!input.trim() || sending}>
                      {sending ? <Loader2 size={15} className="spin" /> : <Send size={15} />}
                      {sending ? "Running" : "Run agent"}
                    </button>
                  </div>
                </div>
              </form>
            </div>
          </div>

          <aside className="inspector">
            <div className="inspector-head">
              <span>RUNTIME</span>
              <Activity size={14} />
            </div>
            <div className={`runtime-status ${system}`}>
              <span className="status-dot large" />
              <div>
                <strong>{system === "online" ? "Online" : system === "checking" ? "Checking" : "Offline"}</strong>
                <small>{backendUpdated ? `Updated ${backendUpdated}` : "Connection status"}</small>
              </div>
            </div>

            <div className="inspector-block">
              <div className="inspector-label">ACTIVE AGENT</div>
              <div className="inspector-agent">
                <span className="agent-glyph large">{current.glyph}</span>
                <div><strong>{current.label}</strong><small>{current.short}</small></div>
              </div>
            </div>

            <div className="inspector-block">
              <div className="inspector-label">SESSION</div>
              <div className="metric"><span>Messages</span><strong>{sessionMessages.length}</strong></div>
              <div className="metric"><span>Persistence</span><strong>Local</strong></div>
              <div className="metric"><span>Input limit</span><strong>12k chars</strong></div>
            </div>

            <div className="inspector-block">
              <div className="inspector-label">CAPABILITIES</div>
              <div className="capability"><Cpu size={14} /><span>LLM reasoning runtime</span></div>
              <div className="capability"><Database size={14} /><span>Context & memory ready</span></div>
              <div className="capability"><TerminalSquare size={14} /><span>Tool execution path</span></div>
              <div className="capability"><ShieldCheck size={14} /><span>Production API boundary</span></div>
            </div>

            <div className="inspector-note">
              <Bot size={15} />
              <span>The web console is intentionally separated from the agent runtime. Configure the backend through the Vercel environment variables so credentials stay server-side.</span>
            </div>
          </aside>
        </div>
      </section>

      {showSettings && (
        <div className="modal-backdrop" onClick={() => setShowSettings(false)}>
          <div className="settings-modal" onClick={(event) => event.stopPropagation()}>
            <div className="settings-head">
              <div><div className="eyebrow">PROJECT SETTINGS</div><h2>Octic runtime</h2></div>
              <button className="icon-button" onClick={() => setShowSettings(false)}><X size={17} /></button>
            </div>
            <div className="settings-body">
              <div className="setting-row"><span>Backend URL</span><strong>{process.env.NEXT_PUBLIC_OCTIC_AGENT_URL ?? "Server-side environment"}</strong></div>
              <div className="setting-row"><span>Selected agent</span><strong>{current.label}</strong></div>
              <div className="setting-row"><span>Session storage</span><strong>Browser local storage</strong></div>
              <div className="settings-callout"><ShieldCheck size={17} /><span>API credentials are never stored in the browser by this UI.</span></div>
            </div>
          </div>
        </div>
      )}
    </main>
  );
}
