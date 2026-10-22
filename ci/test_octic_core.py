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
from unittest.mock import Mock, patch

from octic_ai_agent import OcticAgent
from octic_ai_agent import cli


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


if __name__ == "__main__":
    unittest.main()
