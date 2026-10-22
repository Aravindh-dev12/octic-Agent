# Octic AI Agent — Docker Setup

This directory contains the primary Octic API container and optional legacy integration containers.

## Requirements

- Docker Engine or Docker Desktop
- Docker Compose v2
- An API key for your chosen model provider

## Run the Octic API

From the repository root, create a random API bearer token and export the provider credentials:

```bash
export OPENAI_API_KEY="your-provider-api-key"
export OCTIC_AI_AGENT_API_TOKEN="$(python -c 'import secrets; print(secrets.token_urlsafe(32))')"
docker compose -f docker/docker-compose.yml config
docker compose -f docker/docker-compose.yml up --build -d api
```

The API is available at `http://localhost:8080`. Check its health and readiness:

```bash
curl http://localhost:8080/health
curl http://localhost:8080/ready
curl http://localhost:8080/agents -H "Authorization: Bearer ${OCTIC_AI_AGENT_API_TOKEN}"
```

Run a chat request:

```bash
curl http://localhost:8080/chat \
  -H "Authorization: Bearer ${OCTIC_AI_AGENT_API_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"message":"Explain how DNS resolution works.","agent":"default"}'
```

Stop the API:

```bash
docker compose -f docker/docker-compose.yml down
```

## Environment settings

- `OPENAI_API_KEY`: credentials for OpenAI when using the default model; use the appropriate provider-specific credentials when selecting another LiteLLM model.
- `OCTIC_AI_AGENT_API_TOKEN`: required bearer token for remote or container access.
- `API_PORT`: optional host port (defaults to 8080).
- `OCTIC_AI_AGENT_MODEL`: optional model override.

Keep these values in your shell or a local, untracked environment file. Never commit provider keys or bearer tokens. Do not expose the API publicly without TLS, strong authentication, and network restrictions.

## Optional legacy integration services

A plain `docker compose up` starts the Octic API only. Legacy UI, chat, and agent services are grouped under the `legacy` profile; the old all-in-one dashboard is isolated in the `claw` profile to prevent port conflicts.

Start a selected legacy UI or chat service only when its dependencies are installed and you need that integration:

```bash
docker compose -f docker/docker-compose.yml --profile legacy up --build -d ui chat
# Or start the previous all-in-one dashboard separately:
docker compose -f docker/docker-compose.yml --profile claw up --build -d claw
```

The standalone Octic API does not require these services. Do not start the legacy dashboard alongside the legacy UI because both use port 8082.
