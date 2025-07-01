import os
import streamlit as st
from google import genai
from google.genai import types


api_key=AIzaSyB6ksqc6ZooJoQHTkj4DH-mL2MA5hhcw6I

model = "gemini-2.5-pro"

st.set_page_config(page_title="NutriPal AI Assistant", layout="centered", initial_sidebar_state="collapsed")

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    .chatbot-box {
        max-width: 400px;
        margin: auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='chatbot-box'>", unsafe_allow_html=True)
st.markdown("""
    <h3 style='text-align: center; margin-bottom: 1rem;'>🤖 NutriPal AI</h3>
""", unsafe_allow_html=True)

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask about your diet 👇", key="user_input")

if st.button("Send") and user_input:
    contents = [
        types.Content(role="user", parts=[types.Part(text="You are NutriPal AI...")]),  # brief system prompt
        types.Content(role="user", parts=[types.Part(text=user_input)])
    ]
    config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=-1),
        response_mime_type="text/plain"
    )
    reply = ""
    for chunk in client.models.generate_content_stream(model=model, contents=contents, config=config):
        reply += chunk.text
    st.session_state.chat_history.append((user_input, reply.strip()))

for user, bot in reversed(st.session_state.chat_history[-5:]):
    st.markdown(f"**🧑 You:** {user}")
    st.markdown(f"**🤖 NutriPal AI:** {bot}")

st.markdown("</div>", unsafe_allow_html=True)
