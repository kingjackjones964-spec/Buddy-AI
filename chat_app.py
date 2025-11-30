# यह लाइन if prompt := st.chat_input("...") के अंदर है
if prompt := st.chat_input("मैं आपकी कैसे मदद कर सकता हूँ?"): 
    # (यूज़र मैसेज का कोड)
    # ...
    
    # AI का जवाब प्राप्त करें (Streaming version)
    with st.chat_message("assistant"):  # <--- इंडेंटेशन स्तर 1
        message_placeholder = st.empty()  # <--- इंडेंटेशन स्तर 2
        full_response = ""
        
        try: # <--- इंडेंटेशन स्तर 2
            response_stream = st.session_state.chat.send_message_streaming(prompt)
            
            for chunk in response_stream: # <--- इंडेंटेशन स्तर 3
                if chunk.text:
                    full_response += chunk.text
                    message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
            
        except Exception as e: # <--- इंडेंटेशन स्तर 2
            full_response = f"माफ़ करना, कनेक्शन में कोई समस्या है। Error: {e}"
            message_placeholder.markdown(full_response)
    
    # AI के जवाब को चैट हिस्ट्री में सेव करें
    st.session_state.messages.append({"role": "assistant", "content": full_response}) # <--- इंडेंटेशन स्तर 1
