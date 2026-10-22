'use client'

import { useState, useEffect, useCallback } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Building2, Users, Shield, DollarSign, Activity, Database, Sparkles, ExternalLink } from 'lucide-react'
import IsometricOffice from '../components/IsometricOffice'
import ActivityLog from '../components/ActivityLog'
import RequestPipeline from '../components/RequestPipeline'
import StatsCards from '../components/StatsCards'
import TeamDashboard from '../components/TeamDashboard'
import SecurityDashboard from '../components/SecurityDashboard'
import DatabaseDashboard from '../components/DatabaseDashboard'
import CostDashboard from '../components/CostDashboard'

const tabs = [
  { id: 'office', label: 'Main Office', icon: Building2 },
  { id: 'mascot', label: '3D Octopus Mascot', icon: Sparkles },
  { id: 'stats', label: 'Interaction Stats', icon: Activity },
  { id: 'team', label: 'Agent Thoughts', icon: Users },
  { id: 'cost', label: 'Cost Savings', icon: DollarSign },
  { id: 'security', label: 'Security', icon: Shield },
  { id: 'database', label: 'Database', icon: Database },
]

export default function Home() {
  const [activeTab, setActiveTab] = useState('office')
  const [headerStats, setHeaderStats] = useState({
    tasks: 128,
    tokens: 4200000,
    savings: 1450,
  })
  const [activeRequest, setActiveRequest] = useState(null)
  
  // Fetch stats for header
  useEffect(() => {
    const fetchHeaderStats = async () => {
      try {
        const response = await fetch('/api/stats')
        if (response.ok) {
          const data = await response.json()
          setHeaderStats({
            tasks: data.allTime?.tasks_completed || 128,
            tokens: data.allTime?.tokens?.total || 4200000,
            savings: Math.round(data.allTime?.savings_usd || 1450),
          })
        }
      } catch (error) {
        // use fallback initial stats
      }
    }
    
    fetchHeaderStats()
    const interval = setInterval(fetchHeaderStats, 30000)
    return () => clearInterval(interval)
  }, [])

  // Handle request updates from pipeline
  const handleRequestUpdate = useCallback((request) => {
    setActiveRequest(request)
  }, [])

  return (
    <main className="min-h-screen p-4 lg:p-6 relative bg-[#0a0714] text-slate-100">
      {/* Header */}
      <motion.header 
        className="flex flex-col lg:flex-row lg:items-center justify-between gap-4 mb-6 pb-4 border-b border-purple-900/40"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
      >
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-3">
            <motion.div 
              className="w-12 h-12 rounded-xl flex items-center justify-center text-2xl border border-purple-500/40 bg-purple-950/60 shadow-lg shadow-purple-950/50"
              whileHover={{ scale: 1.05, rotate: 5 }}
            >
              🐙
            </motion.div>
            <div>
              <h1 className="font-display text-2xl font-bold tracking-tight">
                <span className="text-purple-400">OCTO</span>
                <span className="text-white mx-2">AGENT</span>
                <span className="text-xs px-2 py-0.5 rounded-full bg-purple-900/70 text-purple-300 font-mono border border-purple-700/50">
                  OFFICE
                </span>
              </h1>
              <p className="text-xs text-purple-300/70">Virtual AI Office Dashboard &amp; Multi-Agent Workflow Visualizer</p>
            </div>
          </div>

          <div className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-950/60 border border-emerald-500/50">
            <div className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
            <span className="text-xs text-emerald-400 font-bold">WORKFORCE LIVE</span>
          </div>
        </div>

        {/* Quick stats & 3D Bridge */}
        <div className="flex items-center gap-4 lg:gap-6 text-sm">
          <div className="hidden lg:flex items-center gap-5 text-xs">
            <div>
              <span className="text-purple-400/80">Tasks: </span>
              <span className="text-cyan-400 font-bold font-mono">{headerStats.tasks}</span>
            </div>
            <div>
              <span className="text-purple-400/80">Tokens: </span>
              <span className="text-purple-300 font-bold font-mono">{(headerStats.tokens / 1000000).toFixed(2)}M</span>
            </div>
            <div>
              <span className="text-purple-400/80">Saved: </span>
              <span className="text-emerald-400 font-bold font-mono">${headerStats.savings.toLocaleString()}</span>
            </div>
          </div>

          <a
            href="http://localhost:3000/office"
            target="_blank"
            rel="noreferrer"
            className="flex items-center gap-2 px-3.5 py-1.5 rounded-lg text-xs font-semibold bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white shadow-md shadow-purple-950 transition"
          >
            <span>🎮 Enter 3D Retro Office</span>
            <ExternalLink className="w-3.5 h-3.5" />
          </a>
        </div>
      </motion.header>

      {/* Tab Navigation */}
      <motion.nav 
        className="flex gap-2 mb-6 overflow-x-auto pb-2"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
      >
        {tabs.map((tab) => (
          <motion.button
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            className={`flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium whitespace-nowrap transition-all ${
              activeTab === tab.id
                ? 'bg-purple-900/60 border border-purple-500 text-purple-200 shadow-md shadow-purple-950'
                : 'bg-purple-950/20 border border-purple-900/40 text-purple-300/70 hover:text-white hover:bg-purple-900/30'
            }`}
            whileHover={{ scale: 1.02 }}
            whileTap={{ scale: 0.98 }}
          >
            <tab.icon className="w-4 h-4 text-purple-400" />
            <span>{tab.label}</span>
          </motion.button>
        ))}
      </motion.nav>

      {/* Main Content */}
      <AnimatePresence mode="wait">
        {activeTab === 'office' && (
          <motion.div
            key="office"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="grid grid-cols-1 xl:grid-cols-3 gap-6"
          >
            {/* Office View */}
            <div className="xl:col-span-2">
              <div className="glass-card rounded-xl p-4 h-auto border border-purple-900/40 bg-purple-950/20">
                <IsometricOffice activeRequest={activeRequest} />
              </div>
            </div>

            {/* Sidebar */}
            <div className="space-y-4">
              <RequestPipeline onRequestUpdate={handleRequestUpdate} />
              <ActivityLog />
            </div>
          </motion.div>
        )}

        {activeTab === 'mascot' && (
          <motion.div
            key="mascot"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="rounded-2xl border border-purple-800/40 bg-purple-950/20 overflow-hidden shadow-2xl"
          >
            <div className="p-4 border-b border-purple-900/40 bg-purple-950/40 flex items-center justify-between">
              <div className="flex items-center gap-3">
                <span className="text-2xl">🐙</span>
                <div>
                  <h3 className="text-sm font-bold text-purple-200">Octo Mascot 3D Model</h3>
                  <p className="text-xs text-purple-400/80">Interactive WebGL shader model with mouse gaze tracking &amp; arm wave simulation</p>
                </div>
              </div>
              <a
                href="/mascot/index.html"
                target="_blank"
                rel="noreferrer"
                className="text-xs flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-purple-900/60 hover:bg-purple-800 text-purple-200 transition"
              >
                Fullscreen <ExternalLink className="w-3 h-3" />
              </a>
            </div>
            <div className="h-[650px] w-full bg-[#0c0819]">
              <iframe
                src="/mascot/index.html"
                title="Octo 3D Mascot"
                className="w-full h-full border-0"
              />
            </div>
          </motion.div>
        )}

        {activeTab === 'stats' && (
          <motion.div
            key="stats"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            className="space-y-6"
          >
            <StatsCards />
          </motion.div>
        )}

        {activeTab === 'team' && (
          <motion.div
            key="team"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
          >
            <TeamDashboard />
          </motion.div>
        )}

        {activeTab === 'cost' && (
          <motion.div
            key="cost"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
          >
            <CostDashboard />
          </motion.div>
        )}

        {activeTab === 'security' && (
          <motion.div
            key="security"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
          >
            <SecurityDashboard />
          </motion.div>
        )}

        {activeTab === 'database' && (
          <motion.div
            key="database"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
          >
            <DatabaseDashboard />
          </motion.div>
        )}
      </AnimatePresence>

      {/* Footer */}
      <motion.footer 
        className="mt-8 text-center text-xs text-purple-400/60 pb-4"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1 }}
      >
        <p>Octo Agent © {new Date().getFullYear()} • 3D Autonomous Multi-Agent Workforce &amp; Virtual Office</p>
      </motion.footer>
    </main>
  )
}
