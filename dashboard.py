# dashboard.py
import streamlit as st
from history import get_user_history

def show_dashboard(username):
    st.title(f"📁 {username}'s Dashboard")
    history = get_user_history(username)

    if not history:
        st.info("No history found.")
    else:
        for record in reversed(history):
            st.markdown(f"""
            - **Time**: {record['timestamp']}
            - **DNA Input**: `{record['dna']}`
            """)
