from config import get_openai_or_ollama_client, OPENAI_API_KEY, OPENAI_MODEL
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

def main():
    provider, client, model = get_openai_or_ollama_client()
    if provider == "ollama":
        # Use OpenAI SDK against Ollama's OpenAI-compatible endpoint
        resp = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "Say hello in one short sentence."}],
            temperature=0.2,
        )
        print(resp.choices[0].message.content)
    else:
        # Use LangChain's ChatOpenAI for OpenAI proper
        llm = ChatOpenAI(api_key=OPENAI_API_KEY, model=OPENAI_MODEL)
        resp = llm.invoke([HumanMessage(content="Say hello in one short sentence.")])
        print(resp.content)

if __name__ == "__main__":
    main()
