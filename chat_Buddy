import streamlit as st
from google import genai

# ऐप का Title
st.title("⭐ TezChat AI Assistant")

# Key को सुरक्षित रूप से Streamlit Secrets से लोड करें
# यदि Key नहीं मिलती है, तो ऐप बंद हो जाएगा और एरर देगा
try:
    GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
except KeyError:
    st.error("माफ़ करना, GEMINI_API_KEY Streamlit Secrets में नहीं मिला। कृपया इसे सेट करें।")
    st.stop()

# Gemini Client को Initialize करें
client = genai.Client(api_key=GEMINI_API_KEY)

# चैट हिस्ट्री को बनाए रखें
if "chat" not in st.session_state:
    # हम Gemini मॉडल के साथ बातचीत शुरू करने के लिए एक 'Chat' ऑब्जेक्ट का उपयोग करते हैं
    # इससे AI को पिछली बातें याद रहती हैं (Context)
    st.session_state.chat = client.chats.create(model="gemini-2.5-flash")
    st.session_state.messages = []

# पिछली चैट हिस्ट्री को दिखाएँ
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# यूज़र से इनपुट लें
if prompt := st.chat_input("मैं आपकी कैसे मदद कर सकता हूँ?"):
    
    # यूज़र के मैसेज को चैट हिस्ट्री में जोड़ें और दिखाएँ
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI का जवाब प्राप्त करें
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Gemini API को मैसेज भेजें
            response = st.session_state.chat.send_message(prompt)
            full_response = response.text
        except Exception as e:
            full_response = f"माफ़ करना, कनेक्शन में कोई समस्या है। Error: {e}"

        message_placeholder.markdown(full_response)
        
    # AI के जवाब को चैट हिस्ट्री में सेव करें
    st.session_state.messages.append({"role": "assistant", "content": full_response})

