"""Command-line interface for the standalone Octic AI Agent."""
from __future__ import annotations

import argparse
import os
import sys
from collections.abc import Sequence
from typing import Any

from . import __version__


_DEFAULT_INSTRUCTIONS = "You are Octic AI Agent, a helpful, accurate general-purpose assistant."


def _port(value: str) -> int:
    try:
        port = int(value)
    except ValueError as exc:
        raise argparse.ArgumentTypeError("port must be an integer") from exc
    if not 1 <= port <= 65535:
        raise argparse.ArgumentTypeError("port must be between 1 and 65535")
    return port


def _add_agent_options(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--model", help="LiteLLM model identifier (defaults to OCTIC_AI_AGENT_MODEL or gpt-4o-mini).")
    parser.add_argument("--instructions", default=_DEFAULT_INSTRUCTIONS, help="System instructions for the agent.")
    parser.add_argument("--name", default="OcticAgent", help="Agent display name.")
    parser.add_argument("--max-iterations", type=int, default=8, help="Maximum model turns per prompt (default: 8).")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="octic-ai-agent",
        description="Run Octic AI Agent locally or serve it over HTTP.",
        epilog=(
            "Quick start: export OPENAI_API_KEY=...; "
            "octic-ai-agent run 'Explain how TCP works'."
        ),
    )
    parser.add_argument("--version", action="version", version=f"Octic AI Agent {__version__}")
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Run one prompt and print the response.")
    run_parser.add_argument("prompt", nargs="+", help="The task or question for the agent.")
    _add_agent_options(run_parser)

    chat_parser = subparsers.add_parser("chat", help="Start an interactive conversation.")
    _add_agent_options(chat_parser)

    serve_parser = subparsers.add_parser("serve", help="Run the Octic HTTP API.")
    serve_parser.add_argument("--host", default=os.environ.get("OCTIC_AI_AGENT_API_HOST", "127.0.0.1"))
    serve_parser.add_argument("--port", type=_port, default=int(os.environ.get("OCTIC_AI_AGENT_API_PORT", "8080")))

    subparsers.add_parser("doctor", help="Check the local Octic runtime configuration.")
    return parser


def _agent_from_args(args: Any) -> Any:
    from .agent import OcticAgent
    from .tools import default_tools

    return OcticAgent(
        instructions=args.instructions,
        name=args.name,
        model=args.model,
        tools=default_tools(),
        max_iterations=args.max_iterations,
    )


def _run_chat(agent: Any) -> int:
    print("Octic AI Agent chat. Type 'exit' or 'quit' to finish.")
    while True:
        try:
            prompt = input("you> ").strip()
        except EOFError:
            print()
            return 0
        except KeyboardInterrupt:
            print()
            return 130
        if not prompt:
            continue
        if prompt.lower() in {"exit", "quit"}:
            return 0
        try:
            print(f"octic> {agent.start(prompt)}")
        except Exception as exc:
            print(f"Octic AI Agent error: {exc}", file=sys.stderr)
            return 1


def _doctor() -> int:
    model = (
        os.environ.get("OCTIC_AI_AGENT_MODEL")
        or os.environ.get("OPENAI_MODEL")
        or "gpt-4o-mini"
    )
    key_names = (
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY",
        "GEMINI_API_KEY",
        "GOOGLE_API_KEY",
        "COHERE_API_KEY",
        "MISTRAL_API_KEY",
        "GROQ_API_KEY",
        "DEEPSEEK_API_KEY",
        "OPENROUTER_API_KEY",
        "DASHSCOPE_API_KEY",
        "AWS_ACCESS_KEY_ID",
    )
    detected = [key for key in key_names if os.environ.get(key)]
    try:
        import litellm  # noqa: F401
    except ImportError:
        print("LiteLLM is not installed. Run: python -m pip install octic-ai-agent", file=sys.stderr)
        return 1

    print(f"Octic AI Agent {__version__}")
    print(f"Model: {model}")
    print(f"Provider credentials detected: {', '.join(detected) if detected else 'none'}")
    try:
        from .tools import default_tools
        print(f"Built-in tools: {', '.join(getattr(tool, '__name__', 'tool') for tool in default_tools())}")
    except Exception as exc:
        print(f"Tool configuration error: {exc}", file=sys.stderr)
        return 1
    print(f"Workspace: {os.environ.get('OCTIC_AI_AGENT_WORKSPACE', 'not configured')}")
    print(f"File writes: {'enabled' if os.environ.get('OCTIC_AI_AGENT_ALLOW_FILE_WRITES') == '1' else 'disabled'}")
    print(f"Command execution: {'enabled (not sandboxed)' if os.environ.get('OCTIC_AI_AGENT_ALLOW_COMMANDS') == '1' else 'disabled'}")
    print("Credential presence is checked locally; this command does not make a model request.")
    if not detected and not os.environ.get("OLLAMA_HOST") and not os.environ.get("OPENAI_API_BASE"):
        print(
            "Set the API key for your provider, or configure a local/OpenAI-compatible endpoint.",
            file=sys.stderr,
        )
        return 1
    return 0


def _dispatch_compat_command(command_args: Sequence[str]) -> int:
    """Route extended legacy subcommands only when the optional bridge is installed."""
    try:
        from praisonai.__main__ import main as compat_main
    except ImportError as exc:
        command = " ".join(command_args)
        print(
            f"Command 'octic-ai-agent {command}' belongs to an optional integration. "
            "Install it with 'python -m pip install \"octic-ai-agent[compat]\"' "
            "or use 'octic-ai-agent --help' for core commands.",
            file=sys.stderr,
        )
        print(f"Details: {exc}", file=sys.stderr)
        return 2

    saved_argv = sys.argv[:]
    try:
        sys.argv = [saved_argv[0], *command_args]
        result = compat_main()
        return result if isinstance(result, int) else 0
    except SystemExit as exc:
        return exc.code if isinstance(exc.code, int) else 0
    finally:
        sys.argv = saved_argv


def main(argv: Sequence[str] | None = None) -> int:
    argv_list = list(argv) if argv is not None else sys.argv[1:]
    core_commands = {"run", "chat", "serve", "doctor", "--version", "-h", "--help"}
    if argv_list and not argv_list[0].startswith("-") and argv_list[0] not in core_commands:
        return _dispatch_compat_command(argv_list)
    if (
        len(argv_list) > 1
        and argv_list[0] == "serve"
        and not argv_list[1].startswith("-")
    ):
        # Preserve optional serve modes such as MCP, A2A and recipe servers.
        return _dispatch_compat_command(argv_list)

    parser = build_parser()
    args = parser.parse_args(argv_list)
    if not args.command:
        parser.print_help()
        return 0

    if args.command == "doctor":
        return _doctor()

    if args.command == "serve":
        os.environ["OCTIC_AI_AGENT_API_HOST"] = args.host
        os.environ["OCTIC_AI_AGENT_API_PORT"] = str(args.port)
        try:
            from .api_server import app
        except ImportError as exc:
            print(
                "The Octic HTTP API needs its optional dependencies. Install with "
                "'python -m pip install \"octic-ai-agent[api]\"'.",
                file=sys.stderr,
            )
            print(f"Details: {exc}", file=sys.stderr)
            return 1
        app.run(host=args.host, port=args.port, debug=False, threaded=True)
        return 0

    if args.command == "run":
        try:
            agent = _agent_from_args(args)
            print(agent.start(" ".join(args.prompt)))
            return 0
        except Exception as exc:
            print(f"Octic AI Agent error: {exc}", file=sys.stderr)
            return 1

    if args.command == "chat":
        return _run_chat(_agent_from_args(args))

    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
