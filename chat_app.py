import streamlit as st
from google import genai

st.title("मेरा Buddy AI चैटबॉट 💬")

# 1. API Key चेक करें
if "GEMINI_API_KEY" not in st.secrets:
    st.error("कृपया Streamlit Secrets में GEMINI_API_KEY सेट करें।")
    st.stop()

API_KEY = st.secrets["GEMINI_API_KEY"]

# 2. Gemini client initialize करें
client = genai.Client(api_key=API_KEY)

# 3. Session initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# 4. पिछली चैट दिखाएँ
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 5. Input Box
prompt = st.chat_input("मैं आपकी कैसे मदद कर सकता हूँ?")

if prompt:
    # User message UI + save
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant message placeholder
    with st.chat_message("assistant"):
        msg_box = st.empty()
        full_response = ""

        try:
            # Streaming Response
            response = client.models.generate_content_stream(
                model="gemini-2.5-flash",
                contents=prompt
            )

            for chunk in response:
                if chunk.text:
                    full_response += chunk.text
                    msg_box.markdown(full_response + "▌")

            msg_box.markdown(full_response)

        except Exception as e:
            full_response = f"⚠️ Error: {e}"
            msg_box.markdown(full_response)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": full_response
    })