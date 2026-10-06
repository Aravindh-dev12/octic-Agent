# Octic AI Agent Web Desktop

This directory contains the production web console for Octic AI Agent.

## Local development

```bash
pnpm install
pnpm dev
```

The console expects a server-side `OCTIC_AGENT_API_URL`. Optionally set `OCTIC_AGENT_API_TOKEN` to authenticate requests against the Octic API.

The UI keeps conversation history in browser local storage. Agent execution remains on the Octic backend; the Next.js route proxy keeps the API token on the server side.

## Vercel

Set these Vercel project environment variables:

- `OCTIC_AGENT_API_URL`
- `OCTIC_AGENT_API_TOKEN`

Deploy this directory as a Next.js project with **Root Directory = `web`**.

## Runtime endpoints used

- `GET /health`
- `GET /ready`
- `GET /agents`
- `POST /chat`
