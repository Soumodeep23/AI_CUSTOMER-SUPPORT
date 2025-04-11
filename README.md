# AI_CUSTOMER-SUPPORT
It is an ai driven customer support app 

# 🤖 AI Support Assistant

An interactive multi-agent support assistant built with **LangChain**, **Ollama-based LLMs**, **FAISS vectorstore**, and **Streamlit UI**. It allows users to describe or upload issues and get detailed, friendly troubleshooting solutions based on historical ticket data.

---

## 🚀 Features

- 🧠 **Multi-Agent Architecture**
  - Intent Classification
  - Knowledge Retrieval using FAISS
  - Basic Troubleshooting Suggestions
  - Resolution Confirmation
  
- 🔍 **Retrieval-Augmented Generation (RAG)** with past support ticket data

- 🖼️ **Visual Issue Handling** using image-based support with a vision-enabled LLM (e.g. `granite3.2-vision`)

- 💬 **Conversational Interface** with persistent session-based chat log

- 🕒 **3-Day Chat History Storage** with a clock icon in the sidebar

- 📎 **Image Upload** and processing support (png/jpg/jpeg)

---

## 🛠️ Tech Stack

| Layer        | Tech Used |
|-------------|-----------|
| Backend      | Python, LangChain, FAISS, SQLite |
| LLM          | Ollama (`mistral`, `nomic-embed-text`, `granite3.2-vision`) |
| UI           | Streamlit |
| Embeddings   | Ollama Embeddings |
| Vector Store | FAISS |
| Tools        | Custom SQLite + Image tools |
| Infra        | On-prem setup |

---

## 📂 Folder Structure

support-system/ ├── agents/ │ ├── user_input_agent.py │ ├── retriever_agent.py │ ├── troubleshooting_agent.py │ ├── confirmation_agent.py ├── tools/ │ ├── rag_vectorstore.py │ └── sqlite_tool.py ├── chat_history.py ├── vision_agent.py ├── ticket_agent.py ├── build_vectorstore.py ├── Historical_ticket_data.csv └── streamlit_app.py

ollama run mistral
ollama run granite3.2-vision
ollama pull nomic-embed-text

python build_vectorstore.py
streamlit run streamlit_app.py
