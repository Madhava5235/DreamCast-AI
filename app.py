import streamlit as st
import requests
import json

# Groq API Configuration
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Function to query Groq API with user prompt
def query_groq(user_prompt):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "meta-llama/llama-4-scout-17b-16e-instruct",  # Use the appropriate Groq model
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

# Streamlit App UI
st.set_page_config(page_title="Groq Chat UI", page_icon="🤖", layout="centered", initial_sidebar_state="collapsed")
st.markdown(
    """
    <style>
    .big-font {
        font-size: 30px !important;
        font-weight: bold;
        text-align: center;
        color: #4CAF50;
    }
    .animated-box {
        animation: fadeIn 1.5s ease-in-out;
    }
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(-10px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="big-font animated-box">💬 Ask Groq Anything!</div>', unsafe_allow_html=True)
st.markdown("#### Powered by LLaMA 3 on Groq")

# Text area for user input
user_input = st.text_area("📌 Enter your prompt below:", height=150, placeholder="e.g., Give me a sustainable reuse idea for concrete blocks...")

# Generate button
if st.button("🚀 Generate Response"):
    if user_input.strip():
        with st.spinner("Thinking... 🤖"):
            response = query_groq(user_input)
            st.markdown("### ✨ Groq's Response:")
            st.markdown(f"<div class='animated-box'>{response}</div>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a prompt to get started!")
