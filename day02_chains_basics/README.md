# Day 02 — Chains Basics

**Goal:** Build a simple SequentialChain; input/output variables.

## What are LangChain chains?

Chains are LangChain's way of composing multiple LLM- or tool-powered steps into a single reusable workflow. Instead of calling a model once and manually post-processing the response, a chain lets you describe the series of operations that should happen for every invocation. Each link in the chain receives structured inputs, performs its logic (prompt formatting, calling an LLM, parsing output, storing state, etc.), and hands structured outputs to the next link. This makes it easy to encapsulate common patterns like "take a question, look up context, generate an answer" in a single object.

## Why you need chains

* **Encapsulation & reuse:** When you wrap a multi-step pipeline in a chain, you can reuse it like a function without repeating the orchestration code.
* **Consistency:** Input and output keys are explicitly defined, so the pipeline behaves the same way every time.
* **Composability:** Chains can call other chains, memory modules, tools, or even external APIs. This lets you assemble sophisticated applications from small building blocks.
* **Observability:** LangChain tracks intermediate steps, making debugging and tracing easier than ad-hoc scripts.

## Sequential chains in practice

A `SequentialChain` is the simplest chain type. It executes each step in order, passing along the outputs.

1. **Define prompt templates** that describe how inputs should be transformed for the language model.
2. **Create LLM or tool steps** (e.g., `LLMChain`, `Tool`, or custom callables) that consume those prompts.
3. **Specify input/output variables** so LangChain knows which values to expect from the user and which ones to expose from the chain.
4. **Run the chain** with a dictionary that matches the declared input keys. The result is a dictionary of all outputs produced during execution.

This project demonstrates that flow: we configure the environment keys, define a couple of `LLMChain` steps, connect them with `SequentialChain`, and run `main.py` to see how intermediate results move through the pipeline.

## Run

```bash
python main.py
# or open notebook.ipynb
```

## Notes

- Configure keys in the project `.env`.
- Set `OLLAMA_BASE_URL` to route to Ollama (OpenAI-compatible endpoint).
