# auth.py
import streamlit as st
import json

USER_DB = "users.json"

def load_users():
    try:
        with open(USER_DB, "r") as f:
            return json.load(f)
    except:
        return {}

def save_user(username, password):
    users = load_users()
    users[username] = password
    with open(USER_DB, "w") as f:
        json.dump(users, f)

def login():
    st.sidebar.title("🔐 Login / Register")
    users = load_users()
    choice = st.sidebar.radio("Action", ["Login", "Register"])

    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Submit"):
        if choice == "Login":
            if users.get(username) == password:
                st.session_state["user"] = username
                st.success(f"Welcome {username}!")
                return True
            else:
                st.error("Invalid credentials")
        else:
            save_user(username, password)
            st.success("Registered! Now login.")
    return False
