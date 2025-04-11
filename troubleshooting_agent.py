from langchain_community.llms import Ollama

llm = Ollama(model="mistral")

def suggest_basic_troubleshooting(issue: str) -> str:
    prompt = f"""
You're a helpful and friendly AI support assistant.

A user is facing the following issue:
"{issue}"

Please write a detailed response that includes:
- Clear troubleshooting guidance (2–3 steps if needed)
- A human and conversational tone
- Some explanation for each suggestion so the user understands why it helps
- No unnecessary jargon, but not overly short
- Like how a real support expert would patiently guide the user

Response:
"""
    return llm.invoke(prompt).strip()
