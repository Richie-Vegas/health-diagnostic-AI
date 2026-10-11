# multi_agent_diagnosis/frontend.py

import streamlit as st
import requests

# Configure Streamlit page
st.set_page_config(
    page_title="Multi-Agent Disease Diagnosis",
    page_icon="🩺",
    layout="centered",
)

st.title("🩺 Multi-Agent Disease Diagnosis Chatbot")

st.markdown("""
Welcome to the AI-powered medical assistant!  
This chatbot simulates how multiple specialized medical agents—such as CardioAgent, NeuroAgent, and HypertensionAgent—analyze your symptoms and provide insights.

📝 **Type your symptoms below and see how the multi-agent team responds.**
""")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input (multi-line box)
user_message = st.text_area(
    "Describe your symptoms:",
    height=100,
    placeholder="e.g. I have chest pain and feel dizzy."
)

if st.button("Ask AI") and user_message.strip():
    # Add user's message to chat history
    st.session_state.messages.append({"sender": "user", "text": user_message})

    with st.spinner("Thinking..."):
        try:
            # Send message to FastAPI backend
            response = requests.post(
                "http://127.0.0.1:8000/chat",
                json={"user_message": user_message},
                timeout=10
            )
            response.raise_for_status()
            reply = response.json()["reply"]

        except requests.exceptions.RequestException as e:
            reply = f" Error contacting backend: {str(e)}"

    # Add agent's reply to chat history
    st.session_state.messages.append({"sender": "agent", "text": reply})

# Display conversation
for msg in st.session_state.messages:
    if msg["sender"] == "user":
        st.markdown(f"""
            <div style="background-color:#1976d2; color:white; padding:10px; border-radius:5px; margin-bottom:10px;">
                <b> You:</b><br>{msg['text']}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="background-color:#388e3c; color:white; padding:10px; border-radius:5px; margin-bottom:10px;">
                <b>🤖 AI Diagnosis:</b><br>{msg['text']}
            </div>
        """, unsafe_allow_html=True)
# Display conversation with newest first
for msg in reversed(st.session_state.messages):
    if msg["sender"] == "user":
        st.markdown(f"""
            <div style="background-color:#1976d2; color:white; padding:10px; border-radius:5px; margin-bottom:10px;">
                <b> You:</b><br>{msg['text']}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div style="background-color:#388e3c; color:white; padding:10px; border-radius:5px; margin-bottom:10px;">
                <b>🤖 AI Diagnosis:</b><br>{msg['text']}
            </div>
        """, unsafe_allow_html=True)
