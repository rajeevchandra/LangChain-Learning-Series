# Day 01 — Intro to LangChain

**Goal:** Run a simple Hello-World with LangChain, test your environment setup, and generate your first completion.

---

## What is LangChain?
LangChain is a Python framework that streamlines building applications powered by large language models (LLMs). It provides ready-to-use building blocks—such as prompt templates, model wrappers, memory, tools, and chains—that simplify connecting models to external data sources and orchestrating multi-step workflows. By composing these components you can create conversational agents, document question-answering systems, data pipelines, and other intelligent applications without having to manage low-level API details yourself.

At a high level, LangChain focuses on three core ideas:

1. **Integration:** unify access to many LLM providers (OpenAI, Anthropic, local models, etc.) through a consistent interface.
2. **Orchestration:** make it easy to structure complex prompt flows, tool calls, and retrieval steps.
3. **Customization:** let you extend or swap components so solutions can be tuned to your domain, data, or infrastructure.

This introduction day focuses on validating your environment so you can confidently build richer chains in later modules.

---

## Prerequisites
- Python 3.9+
- Virtual environment with requirements installed:
  ```bash
  python -m venv .venv
  source .venv/bin/activate   # Windows: .venv\Scripts\activate
  pip install -r requirements.txt
  ```

---

## Running with OpenAI
1. Copy `.env.example` to `.env`.
2. Set your key in `.env`:
   ```env
   OPENAI_API_KEY=sk-xxxx
   OPENAI_MODEL=gpt-4o-mini
   ```
3. Run:
   ```bash
   cd day01_intro
   python main.py
   ```

---

## Running with Ollama (local model)
1. [Install Ollama](https://ollama.com/download).
2. Pull a lightweight model (example: **llama3.2:1b**):
   ```bash
   ollama pull llama3.2:1b
   ```
   ✅ This is a small model that runs quickly on CPU for basic testing.
3. Update `.env`:
   ```env
   OLLAMA_BASE_URL=http://localhost:11434/v1
   OLLAMA_MODEL=llama3.2:1b
   ```
4. Run:
   ```bash
   cd day01_intro
   python main.py
   ```
   or open the notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```

---

## Expected Output
You should see something like:
```
Hello
```

---

## What this program does
- Loads your configuration (`.env`) for either OpenAI or Ollama.
- Sends a simple prompt: `"Say hello in one short sentence."`
- Prints the model’s response (usually just `"Hello"` or `"Hello there!"`).

This verifies that:
- Your environment is set up correctly.
- LangChain (for OpenAI) or Ollama (local) is responding.
- You can run completions end-to-end before moving on.

## Notes
- If `OLLAMA_BASE_URL` is set, the code automatically routes to Ollama’s OpenAI-compatible endpoint.
- Otherwise, it defaults to OpenAI’s API.
- This day is just a **sanity check**. From Day 2 onward, we’ll start chaining prompts and building richer examples.
