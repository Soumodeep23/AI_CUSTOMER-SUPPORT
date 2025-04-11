import streamlit as st
from PIL import Image
from io import BytesIO

from chat_history import save_chat, load_recent_chats, clean_old_chats
from ticket_agent import query_ticket_knowledgebase
from vision_agent import handle_image_query

# Setup
st.set_page_config(page_title="Support Assistant", layout="wide")
clean_old_chats()

# Initialize session state
if "chat_log" not in st.session_state:
    st.session_state.chat_log = [("🧠 AI Support Assistant", "Hi there! How can I help you today? 😊")]

# Sidebar Chat History
with st.sidebar:
    st.markdown("### 🕒 Chat History")
    for message, reply in st.session_state.chat_log[-10:]:
        st.markdown(f"**You:** {message}")
        st.markdown(f"**AI:** {reply}")
        st.markdown("---")

# Main Interface
st.title("🧠 AI Support Assistant")

# Input area
user_input = st.text_input("Type your message here:")
uploaded_image = st.file_uploader("Attach an image (optional)", type=["jpg", "png", "jpeg"])

# Submit button
if st.button("Send"):
    if not user_input.strip() and not uploaded_image:
        st.warning("Please type a message or upload an image.")
    else:
        if uploaded_image:
            image = Image.open(BytesIO(uploaded_image.read()))
            response = handle_image_query(user_input or "Please describe this image", image)
        else:
            response = query_ticket_knowledgebase(user_input)

        st.session_state.chat_log.append((user_input, response))
        save_chat(user_input, response)

# Display chat log
st.markdown("---")
for message, reply in st.session_state.chat_log:
    st.markdown(f"**🧑 You:** {message}")
    st.markdown(f"**🤖 AI:** {reply}")
    st.markdown("---")
