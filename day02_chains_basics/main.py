from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from config import OPENAI_API_KEY, OPENAI_MODEL, OLLAMA_BASE_URL, OLLAMA_MODEL

def make_llm():
    if OLLAMA_BASE_URL:
        return ChatOpenAI(api_key="ollama", base_url=OLLAMA_BASE_URL, model=OLLAMA_MODEL)
    return ChatOpenAI(api_key=OPENAI_API_KEY, model=OPENAI_MODEL)

def main():
    tmpl = ChatPromptTemplate.from_messages([("system", "You are a helpful assistant."),
                                             ("human", "Summarize: {text}")])
    llm = make_llm()
    chain = tmpl | llm
    print(chain.invoke({"text": "LangChain lets you compose LLM apps"}).content)

if __name__ == "__main__":
    main()
