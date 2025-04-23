import streamlit as st
import json
from hashlib import sha256

def hash_pw(pw): return sha256(pw.encode()).hexdigest()

def load_users():
    with open("users.json", "r", encoding="utf-8") as f:
        return json.load(f)

def save_users(users):
    with open("users.json", "w", encoding="utf-8") as f:
        json.dump(users, f, indent=4)

def authenticate(username, password, users):
    user = users.get(username)
    if user and user["password"] == hash_pw(password):
        return user["role"], user.get("first_login", False)
    return None, None

def update_password(username, new_password, users):
    if username in users:
        users[username]["password"] = hash_pw(new_password)
        users[username]["first_login"] = False
        save_users(users)
        return True
    return False

def show_login():
    users = load_users()
    st.title("Login")
    u = st.text_input("Utilizador")
    p = st.text_input("Palavra-passe", type="password")
    if st.button("Entrar"):
        role, first = authenticate(u, p, users)
        if role:
            st.session_state.update({
                "logged_in": True, "username": u, "role": role, "first_login": first
            })
            st.rerun()
        else:
            st.error("Credenciais inválidas.")
