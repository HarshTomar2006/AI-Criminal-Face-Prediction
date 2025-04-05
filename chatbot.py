# chatbot.py
import streamlit as st
import random

def get_response(msg):
    basic_faq = {
        "what is this": "This predicts a face using DNA-like input using AI.",
        "how it works": "It maps genetic traits to a face using GAN-based models.",
        "who made this": "Made during a hackathon by Harsh Tomar.",
    }
    msg = msg.lower()
    for q in basic_faq:
        if q in msg:
            return basic_faq[q]
    return random.choice(["Hmm interesting...", "Tell me more!", "Cool!", "That's awesome!"])

def chatbot_ui():
    st.sidebar.title("💬 Ask Assistant")
    user_input = st.sidebar.text_input("Ask me anything...")
    if user_input:
        reply = get_response(user_input)
        st.sidebar.info(reply)
