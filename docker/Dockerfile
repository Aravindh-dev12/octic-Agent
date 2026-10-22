# Octic AI Agent standalone HTTP API container.
# Build: docker build -f docker/Dockerfile -t octic-ai-agent-api .
# Run:   docker run -p 8080:8080 -e OPENAI_API_KEY=... -e OCTIC_AI_AGENT_API_TOKEN=... octic-ai-agent-api

FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    OCTIC_AI_AGENT_API_HOST=0.0.0.0 \
    OCTIC_AI_AGENT_API_PORT=8080 \
    OCTIC_AI_AGENT_API_AUTH=enabled

WORKDIR /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends curl \
    && rm -rf /var/lib/apt/lists/*

COPY src/octic_ai_agent /tmp/octic_ai_agent
RUN python -m pip install --no-cache-dir "/tmp/octic_ai_agent[api]" gunicorn \
    && rm -rf /tmp/octic_ai_agent

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD curl --fail http://127.0.0.1:8080/health || exit 1

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "1", "--threads", "4", "octic_ai_agent.api_server:app"]
