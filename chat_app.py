# chat_app.py की शुरुआत में यह जोड़ें
import streamlit as st
from google import genai # या जो भी आपकी API लाइब्रेरी है

# 1. कॉन्फ़िगरेशन (यह आपकी API Key सेट करता है)
if "GEMINI_API_KEY" not in st.secrets:
    st.error("कृपया Streamlit Secrets में GEMINI_API_KEY सेट करें।")
else:
    # API Key सेट करें
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 2. मॉडल और चैट की शुरुआत
if "chat" not in st.session_state:
    # मॉडल चुनें
    model = "gemini-2.5-flash" 
    
    # चैट हिस्ट्री के साथ चैट शुरू करें
    st.session_state.chat = genai.GenerativeModel(model).start_chat(history=[])
    st.session_state.messages = []

st.title("मेरा AI चैटबॉट 💬")
