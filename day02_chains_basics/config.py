from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b-instruct")

def get_openai_or_ollama_client():
    """Return (provider, client, model_name)."""
    from openai import OpenAI
    if OLLAMA_BASE_URL:
        return "ollama", OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama"), OLLAMA_MODEL
    else:
        return "openai", OpenAI(api_key=OPENAI_API_KEY), OPENAI_MODEL
