"""Offline tests for Octic's independent agent runtime and CLI."""
from __future__ import annotations

import asyncio
import contextlib
import io
import json
import os
import sys
import types
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import Mock, patch

from octic_ai_agent import OcticAgent
from octic_ai_agent import cli
from octic_ai_agent.tools import calculate, current_datetime, default_tools


def _response(content=None, tool_calls=None):
    return {
        "choices": [{
            "message": {
                "content": content,
                "tool_calls": tool_calls or [],
            }
        }]
    }


class OcticAgentTests(unittest.TestCase):
    def setUp(self):
        self.completion = Mock()
        self.litellm = types.ModuleType("litellm")
        self.litellm.completion = self.completion
        self.module_patch = patch.dict(sys.modules, {"litellm": self.litellm})
        self.module_patch.start()
        self.addCleanup(self.module_patch.stop)

    def test_plain_response_uses_octic_runtime_and_model(self):
        self.completion.return_value = _response("Hello from Octic.")
        agent = OcticAgent("Be helpful.", name="TestAgent", model="openai/test-model")
        self.assertEqual(agent.start("Say hello"), "Hello from Octic.")
        kwargs = self.completion.call_args.kwargs
        self.assertEqual(kwargs["model"], "openai/test-model")
        self.assertEqual(kwargs["messages"][0]["role"], "system")
        self.assertIn("TestAgent", kwargs["messages"][0]["content"])
        self.assertEqual(agent.history[-2]["role"], "user")
        self.assertEqual(agent.history[-1]["content"], "Hello from Octic.")

    def test_callable_tool_is_executed_then_model_finishes(self):
        def add(a: int, b: int) -> int:
            """Add two integers."""
            return a + b

        self.completion.side_effect = [
            _response(tool_calls=[{
                "id": "call_add",
                "type": "function",
                "function": {"name": "add", "arguments": '{"a": 2, "b": 3}'},
            }]),
            _response("The sum is 5."),
        ]
        agent = OcticAgent("Use tools when useful.", tools=[add])
        self.assertEqual(agent.start("What is 2 + 3?"), "The sum is 5.")
        self.assertEqual(self.completion.call_count, 2)
        self.assertEqual(self.completion.call_args_list[0].kwargs["tools"][0]["function"]["name"], "add")
        second_messages = self.completion.call_args_list[1].kwargs["messages"]
        tool_messages = [message for message in second_messages if message.get("role") == "tool"]
        self.assertEqual(tool_messages[0]["tool_call_id"], "call_add")
        self.assertEqual(tool_messages[0]["content"], "5")

    def test_history_carries_across_prompts_and_can_be_reset(self):
        self.completion.side_effect = [_response("first"), _response("second")]
        agent = OcticAgent("Remember the conversation.")
        self.assertEqual(agent.start("one"), "first")
        self.assertEqual(agent.start("two"), "second")
        messages = self.completion.call_args_list[1].kwargs["messages"]
        self.assertTrue(any(message.get("content") == "one" for message in messages))
        agent.reset()
        self.assertEqual(agent.history, [])

    def test_seeded_history_is_sent_to_the_model(self):
        self.completion.return_value = _response("continued")
        history = [
            {"role": "user", "content": "Earlier question"},
            {"role": "assistant", "content": "Earlier answer"},
        ]
        agent = OcticAgent("Remember the conversation.", history=history)
        self.assertEqual(agent.start("continue"), "continued")
        messages = self.completion.call_args.kwargs["messages"]
        self.assertIn({"role": "user", "content": "Earlier question"}, messages)
        self.assertIn({"role": "assistant", "content": "Earlier answer"}, messages)

    def test_async_api_uses_same_runtime(self):
        self.completion.return_value = _response("async answer")
        agent = OcticAgent("Be concise.")
        self.assertEqual(asyncio.run(agent.astart("hello")), "async answer")

    def test_validation_and_iteration_limit(self):
        with self.assertRaises(ValueError):
            OcticAgent("")
        agent = OcticAgent("Be helpful.", max_iterations=1, tools=[lambda: "ok"])
        self.completion.return_value = _response(tool_calls=[{
            "id": "call_1",
            "type": "function",
            "function": {"name": "<lambda>", "arguments": "{}"},
        }])
        with self.assertRaisesRegex(RuntimeError, "max_iterations=1"):
            agent.start("run the tool")

    def test_bad_tool_arguments_return_an_error_to_the_model(self):
        def multiply(value: int) -> int:
            return value * 2

        self.completion.side_effect = [
            _response(tool_calls=[{
                "id": "call_multiply",
                "type": "function",
                "function": {"name": "multiply", "arguments": "not-json"},
            }]),
            _response("The tool arguments were invalid."),
        ]
        agent = OcticAgent("Use tools.", tools=[multiply])
        self.assertEqual(agent.start("multiply"), "The tool arguments were invalid.")
        tool_messages = [
            message for message in self.completion.call_args_list[1].kwargs["messages"]
            if message.get("role") == "tool"
        ]
        self.assertIn("Tool error", tool_messages[0]["content"])

    def test_cli_run_calls_octic_agent(self):
        fake_agent = Mock()
        fake_agent.start.return_value = "Octic CLI response"
        output = io.StringIO()
        with patch("octic_ai_agent.cli._agent_from_args", return_value=fake_agent):
            with contextlib.redirect_stdout(output):
                code = cli.main(["run", "say", "hello"])
        self.assertEqual(code, 0)
        self.assertIn("Octic CLI response", output.getvalue())
        fake_agent.start.assert_called_once_with("say hello")

    def test_safe_calculator_and_clock_tools(self):
        self.assertEqual(calculate("12 * (13 + 1)")["result"], 168)
        self.assertEqual(calculate("2 ** 8")["result"], 256)
        with self.assertRaises(ValueError):
            calculate("__import__('os').system('echo unsafe')")
        with self.assertRaises(ValueError):
            calculate("10 ** 999999")
        current = current_datetime("UTC")
        self.assertEqual(current["timezone"], "UTC")
        self.assertIn("T", current["datetime"])
        with self.assertRaises(ValueError):
            current_datetime("Definitely/Not_A_Timezone")

    def test_workspace_tools_are_scoped_and_opt_in(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("Octic project", encoding="utf-8")
            (root / ".env").write_text("API_KEY=do-not-read", encoding="utf-8")
            (root / ".env.example").write_text("API_KEY=replace-me", encoding="utf-8")
            (root / ".git").mkdir()
            (root / ".git" / "config").write_text("secret", encoding="utf-8")
            env = {
                "OCTIC_AI_AGENT_WORKSPACE": str(root),
                "PATH": os.environ.get("PATH", ""),
            }
            with patch.dict(os.environ, env, clear=True):
                os.environ.pop("OCTIC_AI_AGENT_ALLOW_FILE_WRITES", None)
                os.environ.pop("OCTIC_AI_AGENT_ALLOW_COMMANDS", None)
                tools = {tool.__name__: tool for tool in default_tools()}
                self.assertIn("calculate", tools)
                self.assertIn("current_datetime", tools)
                self.assertIn("list_workspace_files", tools)
                self.assertIn("read_workspace_file", tools)
                self.assertNotIn("write_workspace_file", tools)
                self.assertNotIn("run_workspace_command", tools)
                self.assertEqual(tools["read_workspace_file"]("README.md"), "Octic project")
                listed = tools["list_workspace_files"]()
                self.assertIn("README.md", listed)
                self.assertIn(".env.example", listed)
                self.assertNotIn(".env", listed)
                self.assertFalse(any(path.startswith(".git/") for path in listed))
                with self.assertRaises(ValueError):
                    tools["read_workspace_file"](".env")
                with self.assertRaises(ValueError):
                    tools["read_workspace_file"]("../outside.txt")

                with patch.dict(os.environ, {"OCTIC_AI_AGENT_ALLOW_FILE_WRITES": "1"}):
                    write_tools = {tool.__name__: tool for tool in default_tools()}
                    with self.assertRaises(FileExistsError):
                        write_tools["write_workspace_file"]("README.md", "replace")
                    write_tools["write_workspace_file"]("notes/result.txt", "created by Octic")
                    self.assertEqual(
                        (root / "notes" / "result.txt").read_text(encoding="utf-8"),
                        "created by Octic",
                    )

                with patch.dict(os.environ, {"OCTIC_AI_AGENT_ALLOW_COMMANDS": "1"}):
                    command_tools = {tool.__name__: tool for tool in default_tools()}
                    result = command_tools["run_workspace_command"](
                        [sys.executable, "-c", "print('tool-ok')"],
                        timeout_seconds=5,
                    )
                    self.assertEqual(result["return_code"], 0)
                    self.assertIn("tool-ok", result["stdout"])

    def test_optional_legacy_command_is_routed_through_octic_cli(self):
        import types as module_types

        package = module_types.ModuleType("praisonai")
        package.__path__ = []
        legacy = module_types.ModuleType("praisonai.__main__")
        legacy.main = Mock(return_value=0)
        original_argv = sys.argv[:]
        with patch.dict(sys.modules, {"praisonai": package, "praisonai.__main__": legacy}):
            code = cli.main(["onboard", "--help"])
        self.assertEqual(code, 0)
        self.assertEqual(sys.argv, original_argv)
        legacy.main.assert_called_once_with()

    def test_missing_compat_layer_reports_install_command(self):
        output = io.StringIO()
        with patch.dict(sys.modules, {"praisonai": None, "praisonai.__main__": None}):
            with contextlib.redirect_stderr(output):
                code = cli.main(["onboard"])
        self.assertEqual(code, 2)
        self.assertIn("octic-ai-agent[compat]", output.getvalue())


if __name__ == "__main__":
    unittest.main()
