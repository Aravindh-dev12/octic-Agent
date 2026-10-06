import { NextRequest, NextResponse } from "next/server";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

const BACKEND_URL = process.env.OCTIC_AGENT_API_URL?.replace(/\/$/, "");
const TOKEN = process.env.OCTIC_AGENT_API_TOKEN;

function unavailable() {
  return NextResponse.json(
    {
      error:
        "Octic backend is not configured. Set OCTIC_AGENT_API_URL on the Vercel project.",
    },
    { status: 503 },
  );
}

async function backend(path: string, init: RequestInit = {}) {
  if (!BACKEND_URL) return unavailable();

  const headers = new Headers(init.headers);
  headers.set("Accept", "application/json");
  if (TOKEN) headers.set("Authorization", `Bearer ${TOKEN}`);

  try {
    const response = await fetch(`${BACKEND_URL}${path}`, {
      ...init,
      headers,
      cache: "no-store",
      signal: AbortSignal.timeout(45_000),
    });

    const body = await response.text();
    const contentType = response.headers.get("content-type") ?? "application/json";
    return new NextResponse(body, {
      status: response.status,
      headers: {
        "content-type": contentType,
        "cache-control": "no-store, max-age=0",
      },
    });
  } catch {
    return NextResponse.json(
      {
        error:
          "Unable to reach the Octic agent backend. Check OCTIC_AGENT_API_URL and backend availability.",
      },
      { status: 502 },
    );
  }
}

export async function GET(request: NextRequest) {
  const action = request.nextUrl.searchParams.get("action") ?? "health";
  if (action === "health") return backend("/health");
  if (action === "ready") return backend("/ready");
  if (action === "agents") return backend("/agents");
  return NextResponse.json({ error: "unknown action" }, { status: 400 });
}

export async function POST(request: NextRequest) {
  if (!BACKEND_URL) return unavailable();
  let payload: unknown;
  try {
    payload = await request.json();
  } catch {
    return NextResponse.json({ error: "invalid JSON" }, { status: 400 });
  }

  if (
    !payload ||
    typeof payload !== "object" ||
    typeof (payload as Record<string, unknown>).message !== "string"
  ) {
    return NextResponse.json(
      { error: "message must be a non-empty string" },
      { status: 400 },
    );
  }

  return backend("/chat", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify(payload),
  });
}
