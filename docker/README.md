# Octic AI Agent — Docker Setup

This directory contains optional container and Compose configurations for local development and service deployment.

## Requirements

- Docker Engine or Docker Desktop
- Docker Compose v2
- Credentials for the model provider used by your configuration

## Start the primary service

Run these commands from the repository root. Replace the placeholder with your own provider key; do not commit it to the repository.

    export OPENAI_API_KEY="your-api-key"
    docker compose -f docker/docker-compose.yml config
    docker compose -f docker/docker-compose.yml up --build -d claw

View logs:

    docker compose -f docker/docker-compose.yml logs -f claw

Stop the service:

    docker compose -f docker/docker-compose.yml down

## Other Compose services

The Compose file also defines optional UI, chat, API, and agent services. Check the service definitions and required environment variables before starting them; do not start every service blindly if ports overlap.

For local development overrides, inspect docker/docker-compose.dev.yml. Bot integration examples are in docker/bots/.

## Security notes

- Supply credentials through environment variables or a local, untracked environment file.
- Never bake API keys into images or Dockerfiles.
- Avoid exposing development ports to untrusted networks.
- Review mounted directories and container permissions before running workloads that execute agent-generated code.

## Troubleshooting

Use docker compose config to validate the configuration before starting containers. Use docker compose logs to inspect service startup errors, and rebuild after changing a Dockerfile or dependency list.
