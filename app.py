import streamlit as st
import requests
import json

# Amas AI (Groq) API Configuration
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

# Function to query Amas AI API
def query_amas_ai(user_prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": GROQ_MODEL,
        "messages": [
            {"role": "system", "content": "You are a helpful and creative assistant."},
            {"role": "user", "content": user_prompt}
        ]
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

# User input
user_input = st.text_input("💬 Type your message:", placeholder="Ask anything...")

# Send message
if st.button("📨 Send") and user_input.strip():
    with st.spinner("Amas AI is thinking..."):
        response = query_amas_ai(user_input)

    st.markdown(f"<div class='chat-bubble user-bubble'><strong>You:</strong> {user_input}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='chat-bubble assistant-bubble'><strong>Amas AI:</strong> {response}</div>", unsafe_allow_html=True)
