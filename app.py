import streamlit as st
from streamlit_option_menu import option_menu
from page.chatbot import chatbot
st.set_page_config(page_title="Konsultasi Dokter")

def main():
    with st.sidebar:
        st.title("Tempat kamu menemukan solusi tentang kesehatan")
        selected = option_menu(
            menu_title="Menu",
            options=["Konsultasi"],
            icons=["robot"],
            menu_icon="cast",
            default_index=0
        )
    if selected == "Konsultasi":
        chatbot()

if __name__ == "__main__":
    main()