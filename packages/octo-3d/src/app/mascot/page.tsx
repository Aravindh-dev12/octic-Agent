"use client";

import React, { useState, useEffect } from "react";
import Link from "next/link";
import { ArrowLeft, Play, Shield, Terminal, Users, Sparkles, RefreshCw, Cpu, Activity, Box } from "lucide-react";

export default function MascotPage() {
  const [activeTab, setActiveTab] = useState<"mascot" | "workforce">("mascot");
  const [agentThought, setAgentThought] = useState("Connected to 3D Model Creation Engine. Ready to generate 3D spatial models...");
  const [isWaving, setIsWaving] = useState(true);

  useEffect(() => {
    const thoughts = [
      "Octo 3D: Walkable retro office rendered with interactive agent desks.",
      "Chief Octo: Ready to synthesize procedural 3D models and agent avatars.",
      "Octo 3D Studio: Connected agents to real-time WebGL 3D model generation.",
      "Spatial Presence: 3D geometry primitives assembled with PBR materials.",
      "Octo Mascot: Tracking cursor and orchestrating 3D workforce state."
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
          <Link
            href="/create-3d"
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-semibold bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white shadow-md shadow-purple-950 transition"
          >
            <Box className="w-3.5 h-3.5" />
            <span>Agent 3D Model Creation</span>
          </Link>

          <Link
            href="/office/builder"
            className="px-3 py-1.5 rounded-lg text-xs font-medium bg-purple-950/60 border border-purple-700/50 hover:bg-purple-900/60 text-purple-200 transition"
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
              <Users className="w-4 h-4" /> 3D Autonomous Workforce
            </h2>
            <p className="text-xs text-slate-400">
              Octo Agent connects autonomous agents directly to real-time 3D model creation and walkable spaces.
            </p>
          </div>

          {/* Agent Squad Overview */}
          <div className="space-y-3 mb-6">
            <div className="p-3 rounded-xl bg-purple-950/40 border border-purple-800/30 hover:border-purple-600/40 transition">
              <div className="flex items-center justify-between text-xs font-semibold mb-1">
                <span className="text-purple-200">3D Modeler Agent</span>
                <span className="text-emerald-400 font-mono">READY</span>
              </div>
              <p className="text-[11px] text-slate-400">Translates prompts into procedural 3D models and avatars.</p>
            </div>

            <div className="p-3 rounded-xl bg-purple-950/40 border border-purple-800/30 hover:border-purple-600/40 transition">
              <div className="flex items-center justify-between text-xs font-semibold mb-1">
                <span className="text-purple-200">3D Spatial Orchestrator</span>
                <span className="text-cyan-400 font-mono">ACTIVE</span>
              </div>
              <p className="text-[11px] text-slate-400">Renders real-time desk avatars and 3D office environments.</p>
            </div>

            <div className="p-3 rounded-xl bg-purple-950/40 border border-purple-800/30 hover:border-purple-600/40 transition">
              <div className="flex items-center justify-between text-xs font-semibold mb-1">
                <span className="text-purple-200">3D Mascot Engine</span>
                <span className="text-pink-400 font-mono">GLTF / WASM</span>
              </div>
              <p className="text-[11px] text-slate-400">8-tentacle procedural wave physics and gaze tracking.</p>
            </div>
          </div>

          {/* Quick Actions */}
          <div className="mt-auto space-y-2 pt-4 border-t border-purple-900/40">
            <Link
              href="/create-3d"
              className="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl font-semibold text-xs bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white shadow-lg shadow-purple-900/30 transition"
            >
              <Box className="w-3.5 h-3.5" /> Agent 3D Model Creation Studio
            </Link>

            <Link
              href="/office"
              className="w-full flex items-center justify-center gap-2 py-2.5 px-4 rounded-xl font-semibold text-xs bg-purple-950/80 border border-purple-700/50 hover:bg-purple-900/60 text-purple-200 transition"
            >
              <Play className="w-3.5 h-3.5" /> Enter 3D Retro Office
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
