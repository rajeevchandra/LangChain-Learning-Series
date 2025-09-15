# Day 01 — Intro to LangChain

**Goal:** Run a simple Hello-World with LangChain, test your environment setup, and generate your first completion.

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

## Notes
- If `OLLAMA_BASE_URL` is set, the code automatically routes to Ollama’s OpenAI-compatible endpoint.
- Otherwise, it defaults to OpenAI’s API.
- This day is just a **sanity check**. From Day 2 onward, we’ll start chaining prompts and building richer examples.
