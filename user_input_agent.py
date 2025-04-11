# agents/user_input_agent.py
from langchain_community.llms import Ollama

llm = Ollama(model="mistral")

def classify_user_intent(user_input: str) -> str:
    prompt = f"""
You are an AI assistant. Classify the user's intent into one of these:
1. AskSolution
2. AskTicketStatus
3. GeneralGreeting
4. Frustration

Input: {user_input}
Intent:"""
    return llm.invoke(prompt).strip()
