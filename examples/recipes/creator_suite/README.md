# Octic AI Agent — Creator Suite Examples

Runnable examples for the Octic AI Agent creator-automation recipes.

## Quick start

From this directory, set the model provider key and run an example:

```bash
export OPENAI_API_KEY="your-api-key"
python news_crawler_example.py
python script_writer_example.py
python hook_generator_example.py
python brief_generator_example.py
```

## Examples

| Example | Description | API key |
|---|---|---|
| `news_crawler_example.py` | Collect AI news from multiple sources | Not required for the listed public sources |
| `script_writer_example.py` | Generate scripts for YouTube, X, and LinkedIn | OpenAI |
| `hook_generator_example.py` | Generate attention-grabbing hooks | OpenAI |
| `brief_generator_example.py` | Generate news briefs | OpenAI |

## Configuration

Set required API keys through environment variables. Do not commit secrets to this repository. If the example uses a local `.env` file, keep that file untracked.

## Capabilities

- News collection, deduplication, and ranking
- Context enrichment and brief generation
- Script, story, hook, and call-to-action generation
- Fact-checking and content packaging
- Screenshot and screen-recording integrations
- Video and voiceover workflows
- Publishing and distribution helpers
- Content-calendar and feedback-analysis workflows

For the overall project overview and development instructions, see the [Octic AI Agent README](../../../README.md).
