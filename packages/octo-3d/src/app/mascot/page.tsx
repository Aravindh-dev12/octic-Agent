"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { ArrowLeft, Play, Shield, Terminal, Users, Sparkles, RefreshCw, Cpu, Activity } from "lucide-react";

export default function MascotPage() {
  const [activeTab, setActiveTab] = useState<"mascot" | "workforce">("mascot");
  const [agentThought, setAgentThought] = useState("Synchronizing 8 containerized agents across virtual office zones...");
  const [isWaving, setIsWaving] = useState(true);

  useEffect(() => {
    const thoughts = [
      "Octo Core: Containerized agent sandbox active on port 4200.",
      "Octo 3D: Walkable retro office rendered with 14 active desks.",
      "Chief Octo: Reviewing pull requests and assigning standup tasks...",
      "NanoClaw Engine: Security isolation verified, filesystem anchored.",
      "Workflow Pipeline: Agent 1 delegated task to DevOps agent.",
      "Octo Mascot: Tracking cursor and orchestrating multi-agent state."
    ];
    let idx = 0;
    const interval = setInterval(() => {
      idx = (idx + 1) % thoughts.length;
      setAgentThought(thoughts[idx]);
    }, 4500);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex flex-col h-screen w-screen bg-[#0d091a] text-slate-100 overflow-hidden font-sans">
      {/* Top Navigation */}
      <header className="flex items-center justify-between px-6 py-3.5 border-b border-purple-900/40 bg-[#120c24]/90 backdrop-blur z-20">
        <div className="flex items-center gap-4">
          <Link
            href="/office"
            className="flex items-center gap-2 px-3 py-1.5 rounded-lg text-sm bg-purple-950/60 border border-purple-800/40 hover:bg-purple-900/60 transition"
          >
            <ArrowLeft className="w-4 h-4 text-purple-300" />
            <span className="text-purple-200">Return to 3D Office</span>
          </Link>
          <div className="h-4 w-px bg-purple-800/40" />
          <div className="flex items-center gap-2.5">
            <span className="text-xl">🐙</span>
            <span className="font-bold text-lg tracking-tight bg-gradient-to-r from-purple-300 via-pink-300 to-sky-300 bg-clip-text text-transparent">
              OCTO AGENT 3D MASCOT
            </span>
            <span className="px-2 py-0.5 text-xs font-semibold rounded-full bg-purple-900/80 text-purple-200 border border-purple-700/50">
              Live WebGL Model
            </span>
          </div>
        </div>

        <div className="flex items-center gap-3">
          <div className="hidden md:flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-950/50 border border-emerald-800/40 text-emerald-400 text-xs">
            <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            <span>Octo Workforce: Active</span>
          </div>
          <Link
            href="/office/builder"
            className="px-3 py-1.5 rounded-lg text-xs font-medium bg-purple-600/30 border border-purple-500/40 hover:bg-purple-600/50 text-purple-100 transition"
          >
            Office Builder
          </Link>
        </div>
      </header>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col lg:flex-row relative overflow-hidden">
        {/* Left / Center 3D Mascot WebGL Canvas Frame */}
        <div className="flex-1 relative bg-gradient-to-b from-[#140d2b] to-[#090514]">
          {/* Real-time WebGL Octopus Viewport */}
          <iframe
            src="/mascot/index.html"
            title="Octo Agent 3D Mascot"
            className="w-full h-full border-0 block"
            sandbox="allow-scripts allow-same-origin"
          />

          {/* Floating Agent Thought Speech Bubble */}
          <div className="absolute bottom-6 left-6 right-6 md:right-auto md:max-w-xl pointer-events-auto">
            <div className="bg-[#1a1236]/90 border border-purple-600/50 rounded-2xl p-4 shadow-2xl backdrop-blur-md">
              <div className="flex items-center gap-2 mb-1.5">
                <span className="text-sm">🐙</span>
                <span className="text-xs font-bold uppercase tracking-wider text-purple-300">
                  Chief Octo Agent Speech
                </span>
                <span className="ml-auto text-[10px] text-purple-400 flex items-center gap-1">
                  <Activity className="w-3 h-3 text-pink-400 animate-pulse" /> Realtime Stream
                </span>
              </div>
              <p className="text-sm text-purple-100 font-medium leading-relaxed">
                "{agentThought}"
              </p>
            </div>
          </div>
        </div>

        {/* Right Sidebar: Workforce Stats & Agent Control */}
        <div className="w-full lg:w-96 border-t lg:border-t-0 lg:border-l border-purple-900/40 bg-[#100a20]/95 flex flex-col p-5 overflow-y-auto z-10">
          <div className="mb-5">
            <h2 className="text-sm font-bold uppercase tracking-wider text-purple-400 mb-1 flex items-center gap-2">
              <Users className="w-4 h-4" /> Autonomous Workforce
            </h2>
            <p className="text-xs text-slate-400">
              Octo Agent combines NanoClaw container isolation with Claw3D retro visualization.
            </p>
          </div>

          {/* Agent Squad Overview */}
          <div className="space-y-3 mb-6">
            <div className="p-3 rounded-xl bg-purple-950/40 border border-purple-800/30 hover:border-purple-600/40 transition">
              <div className="flex items-center justify-between text-xs font-semibold mb-1">
                <span className="text-purple-200">Tentacle #1: Core Orchestrator</span>
                <span className="text-emerald-400 font-mono">ONLINE</span>
              </div>
              <p className="text-[11px] text-slate-400">Routes incoming requests from Slack, Discord, and CLI.</p>
            </div>

            <div className="p-3 rounded-xl bg-purple-950/40 border border-purple-800/30 hover:border-purple-600/40 transition">
              <div className="flex items-center justify-between text-xs font-semibold mb-1">
                <span className="text-purple-200">Tentacle #2: 3D Office Engine</span>
                <span className="text-cyan-400 font-mono">RENDERING</span>
              </div>
              <p className="text-[11px] text-slate-400">Simulates real-time desk avatars, paths, and room presence.</p>
            </div>

            <div className="p-3 rounded-xl bg-purple-950/40 border border-purple-800/30 hover:border-purple-600/40 transition">
              <div className="flex items-center justify-between text-xs font-semibold mb-1">
                <span className="text-purple-200">Tentacle #3: Security Sandbox</span>
                <span className="text-indigo-400 font-mono">CONTAINED</span>
              </div>
              <p className="text-[11px] text-slate-400">Filesystem isolation with Linux container execution.</p>
            </div>

            <div className="p-3 rounded-xl bg-purple-950/40 border border-purple-800/30 hover:border-purple-600/40 transition">
              <div className="flex items-center justify-between text-xs font-semibold mb-1">
                <span className="text-purple-200">Tentacle #4: Workflow Visualizer</span>
                <span className="text-pink-400 font-mono">STREAMING</span>
              </div>
              <p className="text-[11px] text-slate-400">Real-time task chains and cost savings analytics.</p>
            </div>
          </div>

          {/* Quick Actions */}
          <div className="mt-auto space-y-2 pt-4 border-t border-purple-900/40">
            <Link
              href="/office"
              className="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl font-semibold text-xs bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white shadow-lg shadow-purple-900/30 transition"
            >
              <Play className="w-3.5 h-3.5" /> Enter 3D Retro Office
            </Link>

            <a
              href="http://localhost:4200"
              target="_blank"
              rel="noreferrer"
              className="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl font-semibold text-xs bg-purple-950/80 border border-purple-700/50 hover:bg-purple-900/60 text-purple-200 transition"
            >
              <Cpu className="w-3.5 h-3.5" /> Open 2D Isometric Office (Port 4200)
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
