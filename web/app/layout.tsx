import type { Metadata, Viewport } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Octic AI Agent — Autonomous Agent Desktop",
  description: "A production web desktop for running, monitoring and managing Octic AI agents.",
  applicationName: "Octic AI Agent",
  generator: "Octic AI Agent",
  icons: { icon: "/icon.svg" },
};

export const viewport: Viewport = {
  colorScheme: "light",
  themeColor: "#f5f4ee",
};

export default function RootLayout({
  children,
}: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
