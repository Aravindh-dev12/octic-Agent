import './globals.css'

export const metadata = {
  title: 'Octo Office',
  description: 'Octo Agent Office Dashboard & Multi-Agent Visualizer',
}

function NavBar() {
  return (
    <nav className="fixed top-0 left-0 right-0 z-50 bg-[#0d091a]/80 backdrop-blur-sm border-b border-purple-500/30">
      <div className="max-w-7xl mx-auto px-4 h-12 flex items-center justify-between">
        <div className="flex items-center gap-6">
          <span className="text-purple-400 font-bold text-lg">Octo Agent</span>
          <a href="/" className="text-slate-300 hover:text-purple-400 transition-colors text-sm">
            Office
          </a>
        </div>
        <div className="text-slate-500 text-xs">
          3D Multi-Agent Workforce Platform
        </div>
      </div>
    </nav>
  )
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className="min-h-screen cyber-grid relative">
        <div className="cyber-rain" />
        <NavBar />
        <div className="pt-12">
          {children}
        </div>
      </body>
    </html>
  )
}
