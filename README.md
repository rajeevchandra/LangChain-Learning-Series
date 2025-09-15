# LangChain — 30 Days of Hands‑On Projects

This repo is a daily series. Each folder is self-contained with a short README, a runnable `main.py`, **and a Jupyter notebook**.

## LangChain Overview

```mermaid
flowchart LR
  User((User)) -->|"query"| Prompt[Prompt Template]
  Prompt --> Chain[Chain]
  Chain --> LLM((LLM))
  Memory[Memory] -.->|"context"| Chain
  Agent{{Agent}} -.->|"control"| Chain
  Agent --> Tools[(Tools/APIs)]
  Agent --> VectorDB[(Vector DB)]
  LLM -->|"response"| User


**Explanation:**
- **User** sends a query.
- **Prompt Templates** standardize how inputs are passed.
- **Chains** organize calls to LLMs and other modules.
- **Memory** keeps past context available for multi-turn conversations.
- **Agents** decide what to do next (call APIs, query a vector DB, or pass back to the LLM).
- **LLMs** generate responses and send them back to the user.


## How to use
1. Create a virtual env and install deps:
```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pip
pip install -r requirements.txt
```
2. Copy `.env.example` to `.env` and set your keys (or use Ollama/local models).
3. Navigate into any day folder and run `python main.py` or open `notebook.ipynb`.

Contents

- **01. Intro to LangChain** → [day01_intro/notebook.ipynb](day01_intro/notebook.ipynb)
- **02. Chains Basics** → [day02_chains_basics/notebook.ipynb](day02_chains_basics/notebook.ipynb)

03. Prompt Templates → day03_prompt_templates

04. LLM Wrappers → day04_llm_wrappers

05. Memory 101 → day05_memory_101

06. Tools & Agents Intro → day06_tools_agents_intro

07. Mini App → day07_mini_app

08. Document Loaders → day08_doc_loaders

09. Text Splitters → day09_text_splitters

10. Embeddings → day10_embeddings

11. Vector Stores → day11_vectorstores

12. RetrievalQA → day12_retrievalqa

13. RAG + Memory → day13_rag_plus_memory

14. Project: Local Doc Bot → day14_project_local_doc_bot

15. Agents Deep Dive → day15_agents_deep_dive

16. Toolkits → day16_toolkits_sql_python_requests

17. Custom Tools → day17_custom_tools

18. LangGraph Intro → day18_langgraph_intro

19. LangGraph State → day19_langgraph_state

20. LangGraph + Agents → day20_langgraph_agents

21. Project: Research Assistant → day21_project_research_assistant

22. Streaming Outputs → day22_streaming

23. Structured Outputs → day23_structured_outputs

24. Evaluation → day24_evaluation_langsmith

25. Parallelism → day25_parallelism

26. Multi-Model Routing → day26_multi_model_routing

27. RAG Enhancements → day27_rag_enhancements

28. External APIs → day28_external_apis

29. Deployment → day29_deploy_fastapi_docker

30. Final Project → day30_final_project


## Ollama support
- Set `OLLAMA_BASE_URL` in `.env` (default `http://localhost:11434/v1`). Example model:
  ```bash
  ollama pull qwen2.5:7b-instruct
  ```
- Validate your setup:
  ```bash
  python scripts/check_ollama.py
  ```
- When `OLLAMA_BASE_URL` is set, examples auto-route to Ollama via `config.py`.
