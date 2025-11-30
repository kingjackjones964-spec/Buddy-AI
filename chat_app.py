# 1. API Key कॉन्फ़िगरेशन
if "GEMINI_API_KEY" not in st.secrets:
    st.error("कृपया Streamlit Secrets में GEMINI_API_KEY सेट करें।")
else:
    # यहाँ 'else:' के आगे सिर्फ 4 स्पेस हों, उससे ज़्यादा नहीं
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# ... बाकी सेटअप ...

# 2. AI जवाब का ब्लॉक - यह लाइन एकदम बाईं तरफ़ होनी चाहिए!
with st.chat_message("assistant"):
    # यह लाइन 4 स्पेस से Indented होनी चाहिए
    message_placeholder = st.empty() 
    # ... बाकी कोड

import streamlit as st
from google import genai 

# 1. API Key कॉन्फ़िगरेशन (AttributeError को ठीक करता है)
if "GEMINI_API_KEY" not in st.secrets:
    st.error("कृपया Streamlit Secrets में GEMINI_API_KEY सेट करें।")
else:
    # 'secrets' को सही वर्तनी में इस्तेमाल करें
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# 2. मॉडल और चैट की शुरुआत (यदि पहले से नहीं है)
if "chat" not in st.session_state:
    model = "gemini-2.5-flash" 
    # चैट हिस्ट्री के साथ चैट शुरू करें
    st.session_state.chat = genai.GenerativeModel(model).start_chat(history=[])
    st.session_state.messages = []

st.title("मेरा AI चैटबॉट 💬")
