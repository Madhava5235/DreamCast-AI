import streamlit as st
import requests
import json

# Amas AI (Groq) API Configuration
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

# Initialize chat history in session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "system", "content": "You are a helpful and creative assistant."}
    ]

# Function to query Amas AI API
def query_amas_ai(messages):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": GROQ_MODEL,
        "messages": messages
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"⚠ API Error: {response.text}"

# UI Configuration
st.set_page_config(page_title="Amas AI Chat", page_icon="🤖", layout="centered", initial_sidebar_state="collapsed")
st.markdown(
    """
    <style>
    .big-font {
        font-size: 30px !important;
        font-weight: bold;
        text-align: center;
        color: #4CAF50;
    }
    .chat-bubble {
        border-radius: 1rem;
        padding: 0.8rem 1rem;
        margin-bottom: 1rem;
        max-width: 90%;
        word-wrap: break-word;
    }
    .user-bubble {
        background-color: #DCF8C6;
        align-self: flex-end;
        text-align: right;
    }
    .assistant-bubble {
        background-color: #F1F0F0;
        align-self: flex-start;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="big-font">💬 Chat with Amas AI</div>', unsafe_allow_html=True)
st.markdown("##### Powered by LLaMA 3 on Amas AI (Groq)")

# Display conversation history
for msg in st.session_state.chat_history[1:]:  # skip system message
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-bubble user-bubble'><strong>You:</strong> {msg['content']}</div>", unsafe_allow_html=True)
    elif msg["role"] == "assistant":
        st.markdown(f"<div class='chat-bubble assistant-bubble'><strong>Amas AI:</strong> {msg['content']}</div>", unsafe_allow_html=True)

# User input
user_input = st.text_input("💬 Type your message:", placeholder="Ask anything...")

# Send message
if st.button("📨 Send") and user_input.strip():
    # Append user's message
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.spinner("Amas AI is thinking..."):
        response = query_amas_ai(st.session_state.chat_history)

    # Append assistant's reply
    st.session_state.chat_history.append({"role": "assistant", "content": response})

    # Rerun to update display
    st.experimental_rerun()
