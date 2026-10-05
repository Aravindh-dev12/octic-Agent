# Publishing Octic AI Agent

## Hugging Face

The source for the Gradio Space lives in `huggingface_space/`.

The repository workflow `.github/workflows/publish-huggingface.yml` publishes it to:

    Aravindhan11/octic-ai-agent

Required GitHub repository secret:

    HF_TOKEN

`HF_TOKEN` must be a Hugging Face token with write access to create/update Spaces.

Optional GitHub repository variable:

    HF_SPACE_ID

If omitted, the workflow defaults to `Aravindhan11/octic-ai-agent`.

## Kaggle

Run `kaggle/octic_ai_agent_kaggle_smoke.ipynb` for installation/API smoke testing and `kaggle/octic_ai_agent_agent_eval.ipynb` for multi-agent live evaluation.

Live evaluation is disabled unless `OCTIC_KAGGLE_LIVE=1`. API keys must be provided through Kaggle secrets/environment; they are never stored in notebooks.