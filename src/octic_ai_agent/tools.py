"""Safe, opt-in tools used by Octic's standalone agent runtime.

Calculator and clock tools are always available. Web search is enabled when the
optional `search` extra is installed. Workspace access is enabled only when
OCTIC_AI_AGENT_WORKSPACE points at a real directory. Writes and commands each
require a separate explicit opt-in environment variable.
"""
from __future__ import annotations

import ast
import datetime as dt
import importlib.util
import json
import math
import operator
import os
from pathlib import Path
import subprocess
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


_MAX_TEXT_FILE_BYTES = 100_000
_MAX_COMMAND_OUTPUT_CHARS = 12_000
_SKIP_DIRS = {
    ".git", ".hg", ".svn", ".venv", "venv", "env", "__pycache__",
    "node_modules", ".next", "dist", "build", "coverage", ".pytest_cache",
    ".mypy_cache", ".ruff_cache", ".tox", ".aws", ".ssh", ".azure",
    ".kube", ".gnupg", ".docker", ".config", ".local", ".secrets",
}
_SENSITIVE_NAMES = {
    "credentials", "credentials.json", "secrets.json", "id_rsa", "id_ed25519",
    "known_hosts", "authorized_keys", ".npmrc", ".pypirc", ".netrc", "netrc",
    "pip.conf", "npmrc", "service-account.json",
}
_SAFE_ENV_FILES = {".env.example", ".env.sample", ".env.template"}
_BLOCKED_PARTS = {
    ".git", ".hg", ".svn", ".aws", ".ssh", ".azure", ".kube",
    ".gnupg", ".docker", ".config", ".local", ".secrets",
}
_SENSITIVE_MARKERS = (
    "secret", "credential", "password", "passwd", "private_key", "private-key",
    "api_key", "api-key", "apikey", "access_token", "access-token",
    "client_secret", "client-secret", "service_account", "service-account",
)


def calculate(expression: str) -> dict[str, Any]:
    """Evaluate a basic arithmetic expression without executing Python code."""
    if not isinstance(expression, str) or not expression.strip():
        raise ValueError("expression must be a non-empty string.")
    if len(expression) > 240:
        raise ValueError("expression is limited to 240 characters.")

    binary_ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
        ast.Pow: operator.pow,
    }
    unary_ops = {ast.UAdd: operator.pos, ast.USub: operator.neg}

    def visit(node: ast.AST, depth: int = 0) -> int | float:
        if depth > 24:
            raise ValueError("expression is too deeply nested.")
        if isinstance(node, ast.Constant) and type(node.value) in (int, float):
            value = node.value
        elif isinstance(node, ast.UnaryOp) and type(node.op) in unary_ops:
            value = unary_ops[type(node.op)](visit(node.operand, depth + 1))
        elif isinstance(node, ast.BinOp) and type(node.op) in binary_ops:
            left = visit(node.left, depth + 1)
            right = visit(node.right, depth + 1)
            if isinstance(node.op, ast.Pow) and abs(right) > 100:
                raise ValueError("exponents must be between -100 and 100.")
            value = binary_ops[type(node.op)](left, right)
        else:
            raise ValueError("Only numeric constants and +, -, *, /, //, %, **, and parentheses are supported.")

        if type(value) not in (int, float):
            raise ValueError("expression did not produce a number.")
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError("expression produced a non-finite result.")
        if abs(value) > 10**100:
            raise ValueError("result exceeds the supported numeric range.")
        return value

    try:
        tree = ast.parse(expression, mode="eval")
        result = visit(tree.body)
    except (SyntaxError, ZeroDivisionError, OverflowError) as exc:
        raise ValueError(f"invalid arithmetic expression: {exc}") from exc
    return {"expression": expression.strip(), "result": result}


def current_datetime(timezone: str = "UTC") -> dict[str, str]:
    """Return the current local date/time for an IANA time-zone name."""
    if not isinstance(timezone, str) or len(timezone) > 100:
        raise ValueError("timezone must be a valid IANA time-zone name.")
    try:
        zone = ZoneInfo(timezone)
    except (ZoneInfoNotFoundError, ValueError) as exc:
        raise ValueError(f"Unknown time zone: {timezone}") from exc
    current = dt.datetime.now(zone)
    return {
        "timezone": timezone,
        "datetime": current.isoformat(timespec="seconds"),
        "date": current.date().isoformat(),
        "weekday": current.strftime("%A"),
    }


def web_search(
    query: str,
    max_results: int = 5,
    time_limit: str = "",
) -> list[dict[str, str]]:
    """Search the public web; requires the optional ddgs search package."""
    if not isinstance(query, str) or not query.strip():
        raise ValueError("query must be a non-empty string.")
    if len(query) > 500:
        raise ValueError("query is limited to 500 characters.")
    if not isinstance(max_results, int) or isinstance(max_results, bool) or not 1 <= max_results <= 8:
        raise ValueError("max_results must be an integer from 1 to 8.")
    if time_limit not in {"", "d", "w", "m", "y"}:
        raise ValueError("time_limit must be empty, d, w, m, or y.")

    try:
        from ddgs import DDGS
    except ImportError as exc:
        raise RuntimeError(
            "Web search is not installed. Install the optional extra with "
            "'python -m pip install \"octic-ai-agent[search]\"'."
        ) from exc

    results = DDGS(timeout=12).text(
        query=query.strip(),
        safesearch="moderate",
        timelimit=time_limit or None,
        max_results=max_results,
        backend="auto",
    )
    cleaned: list[dict[str, str]] = []
    for item in results or []:
        if not isinstance(item, dict):
            continue
        title = str(item.get("title") or "").strip()
        url = str(item.get("href") or item.get("url") or "").strip()
        snippet = str(item.get("body") or item.get("snippet") or "").strip()
        if not title and not url and not snippet:
            continue
        cleaned.append({
            "title": title[:500],
            "url": url[:2000],
            "snippet": snippet[:2500],
        })
    return cleaned


def _is_sensitive(relative_path: Path) -> bool:
    for part in relative_path.parts:
        lower = part.lower()
        if lower in _BLOCKED_PARTS or lower in {".env"} or lower.startswith(".env."):
            if lower not in _SAFE_ENV_FILES:
                return True
        if lower in _SENSITIVE_NAMES:
            return True
        if any(marker in lower for marker in _SENSITIVE_MARKERS):
            return True
        if lower.startswith(("id_rsa", "id_ed25519")):
            return True
    return relative_path.suffix.lower() in {".pem", ".p12", ".pfx", ".key"}


def _get_workspace_root() -> Path:
    raw = os.environ.get("OCTIC_AI_AGENT_WORKSPACE")
    if not raw:
        raise RuntimeError(
            "Workspace tools are disabled. Set OCTIC_AI_AGENT_WORKSPACE to a directory "
            "you trust before enabling local file tools."
        )
    root = Path(raw).expanduser().resolve()
    if not root.is_dir():
        raise ValueError("OCTIC_AI_AGENT_WORKSPACE must point to an existing directory.")
    return root


def _workspace_path(root: Path, relative: str) -> tuple[Path, Path]:
    if not isinstance(relative, str) or not relative.strip():
        raise ValueError("path must be a non-empty workspace-relative path.")
    requested = Path(relative)
    if requested.is_absolute():
        raise ValueError("use a relative path inside the configured workspace.")
    candidate = (root / requested).resolve()
    try:
        rel = candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError("path escapes the configured workspace.") from exc
    if not rel.parts:
        rel = Path(".")
    if any(part in _BLOCKED_PARTS for part in rel.parts):
        raise ValueError("access to version-control and credential directories is blocked.")
    if _is_sensitive(rel):
        raise ValueError("access to likely secret/key files is blocked.")
    return candidate, rel


def _workspace_tools(root: Path) -> list[Any]:
    def list_workspace_files(path: str = ".", max_results: int = 100) -> list[str]:
        """List workspace-relative text/source file paths without entering caches or dependency folders."""
        if not isinstance(max_results, int) or isinstance(max_results, bool) or not 1 <= max_results <= 200:
            raise ValueError("max_results must be an integer from 1 to 200.")
        start, relative_start = _workspace_path(root, path)
        if not start.is_dir():
            raise ValueError(f"not a directory: {path}")
        found: list[str] = []
        for current, dirs, names in os.walk(start, followlinks=False):
            dirs[:] = sorted(
                name for name in dirs
                if name not in _SKIP_DIRS
                and not (Path(current) / name).is_symlink()
            )
            for name in sorted(names):
                full = Path(current) / name
                try:
                    relative = full.resolve().relative_to(root)
                except (ValueError, OSError):
                    continue
                if _is_sensitive(relative) or full.is_symlink():
                    continue
                found.append(relative.as_posix())
                if len(found) >= max_results:
                    return found
        return found

    def read_workspace_file(path: str) -> str:
        """Read a UTF-8 text file inside the configured workspace (100 KB maximum)."""
        full, _ = _workspace_path(root, path)
        if not full.is_file():
            raise ValueError(f"not a file: {path}")
        size = full.stat().st_size
        if size > _MAX_TEXT_FILE_BYTES:
            raise ValueError(f"file exceeds the {_MAX_TEXT_FILE_BYTES}-byte read limit.")
        try:
            return full.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            raise ValueError("file is not UTF-8 text.") from exc

    def write_workspace_file(path: str, content: str, overwrite: bool = False) -> dict[str, Any]:
        """Create or replace a UTF-8 text file inside the workspace; requires Octic write opt-in."""
        full, _ = _workspace_path(root, path)
        if not isinstance(content, str):
            raise ValueError("content must be text.")
        if len(content.encode("utf-8")) > _MAX_TEXT_FILE_BYTES:
            raise ValueError(f"content exceeds the {_MAX_TEXT_FILE_BYTES}-byte write limit.")
        full.parent.mkdir(parents=True, exist_ok=True)
        # Resolve again after creating parent folders to reject symlink escapes.
        full, relative = _workspace_path(root, path)
        if full.exists() and not overwrite:
            raise FileExistsError(f"{relative.as_posix()} already exists; pass overwrite=true to replace it.")
        full.write_text(content, encoding="utf-8")
        return {"path": relative.as_posix(), "bytes_written": len(content.encode("utf-8"))}

    def run_workspace_command(
        command: list[str],
        timeout_seconds: int = 20,
    ) -> dict[str, Any]:
        """Run a command by argument list inside the configured workspace; requires explicit command opt-in and is not a sandbox."""
        if not isinstance(command, list) or not command or len(command) > 40:
            raise ValueError("command must be a non-empty list of at most 40 arguments.")
        if any(not isinstance(arg, str) or not arg or len(arg) > 2000 for arg in command):
            raise ValueError("each command argument must be non-empty text of at most 2000 characters.")
        if not isinstance(timeout_seconds, int) or isinstance(timeout_seconds, bool) or not 1 <= timeout_seconds <= 60:
            raise ValueError("timeout_seconds must be an integer from 1 to 60.")
        result = subprocess.run(
            command,
            cwd=str(root),
            shell=False,
            capture_output=True,
            text=True,
            timeout=timeout_seconds,
            check=False,
        )
        stdout = result.stdout or ""
        stderr = result.stderr or ""
        return {
            "command": command,
            "return_code": result.returncode,
            "stdout": stdout[:_MAX_COMMAND_OUTPUT_CHARS],
            "stderr": stderr[:_MAX_COMMAND_OUTPUT_CHARS],
            "output_truncated": len(stdout) > _MAX_COMMAND_OUTPUT_CHARS or len(stderr) > _MAX_COMMAND_OUTPUT_CHARS,
        }

    list_workspace_files.__name__ = "list_workspace_files"
    read_workspace_file.__name__ = "read_workspace_file"

    enabled = [list_workspace_files, read_workspace_file]
    if os.environ.get("OCTIC_AI_AGENT_ALLOW_FILE_WRITES") == "1":
        write_workspace_file.__name__ = "write_workspace_file"
        enabled.append(write_workspace_file)
    if os.environ.get("OCTIC_AI_AGENT_ALLOW_COMMANDS") == "1":
        run_workspace_command.__name__ = "run_workspace_command"
        enabled.append(run_workspace_command)
    return enabled


def default_tools() -> list[Any]:
    """Build Octic's built-in tools based on installed extras and explicit local configuration."""
    tools: list[Any] = [calculate, current_datetime]
    try:
        if importlib.util.find_spec("ddgs") is not None:
            tools.append(web_search)
    except (ImportError, ValueError):
        # Keep the base runtime usable if an unusual import hook hides optional packages.
        pass

    workspace = os.environ.get("OCTIC_AI_AGENT_WORKSPACE")
    if workspace:
        tools.extend(_workspace_tools(_get_workspace_root()))
    return tools
