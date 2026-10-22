# Octic AI Agent — Training Integration

This optional integration adds training workflows to Octic AI Agent. It is separate from the standalone core runtime.

## Iterative agent training

Install the compatibility integration:

```bash
python -m pip install -e "src/octic_ai_agent[compat]"
export OPENAI_API_KEY="your-provider-api-key"
```

Run an iterative training loop:

```bash
octic-ai-agent train agents --input "Explain quantum entanglement to a 10-year-old" --iterations 3
octic-ai-agent train list
octic-ai-agent train show SESSION_ID
octic-ai-agent train apply SESSION_ID --run "What about Germany?"
```

Training uses model-generated evaluation/feedback, so its quality depends on the configured provider and rubric. Review generated changes before applying them.

## LLM fine-tuning

The optional `train` extra installs a heavyweight ML stack (including PyTorch and Unsloth). Use it only in a compatible local/GPU environment:

```bash
python -m pip install -e "src/octic_ai_agent[compat,train]"
octic-ai-agent train llm dataset.json --model llama-3.1
```

Check the environment's CUDA/PyTorch compatibility before attempting GPU fine-tuning. API credentials and dataset contents must be managed securely.

## Python interface

The retained trainer currently integrates with the legacy training SDK. Its package/import names are compatibility identifiers; the Octic core itself remains independent of this integration.

For supported core usage, see the repository [README](../../README.md) and [API reference](../../api.md).
