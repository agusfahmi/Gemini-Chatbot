from google import genai
import streamlit as st
from google.genai.types import HttpOptions, ModelContent, Part, UserContent
 
def chatbot():
    st.header('Chatbot Kesehatan')
    st.subheader('Teknologi yang dipakai menggunakan google gemini')
    client = genai.Client(api_key="GOOGLE-API-KEY")
   
    sys_instruct = {
        "role": "doctor",
        "content": "Berikan jawaban yang berbasis fakta medis yang terpercaya, hindari memberikan saran medis yang tidak terverifikasi atau berbahaya. jangan tanggapi pertanyaan diluar medis"
    }

    chat = client.chats.create(
        model="gemini-2.0-flash",
            history=[
        UserContent(parts=[Part(text="Hello")]),
        ModelContent(
            parts=[Part(text="Great to meet you. What would you like to know?")],
        ),
    ],
        )

    def clear_chat_history():
        st.session_state.messages = [{"role": "doctor", "content": "Ada yang bisa AI Bantu?"}]
    st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "doctor", "content":"Ada yang bisa AI Bantu?"}]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Kirim Pesan"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("doctor"):
            with st.spinner("Thinking.."):
                message_placeholder = st.empty()
                try:
                        response = chat.send_message(prompt)
                        full_response = response.text
                except Exception as e:
                        full_response = "Maaf, terjadi kesalahan dalam mendapatkan respons."
            message_placeholder.markdown(full_response)
        st.session_state.messages.append({"role":"doctor", "content": full_response})      
