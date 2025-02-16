import streamlit as st
from ollama._types import ResponseError
from ollama_chat.models import list_models
from ollama_chat.chat.chat_base import ChatBase
from ollama_chat.chat.ollama_chat import OllamaChat

class Ui:
    def __init__(self, chat: ChatBase):
        self.chat = chat
        self.session = st.session_state

    def reset(self):
        self.session["messages"] = []

    def run(self):
        with st.sidebar:
            st.header("Settings")
            st.session_state["model"] = st.selectbox("Model", list_models())

            st.header("Session")
            st.button("Reset", on_click=self.reset)

        st.title("Chat")

        for message in self.chat.get_messages():
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        prompt = st.chat_input("Enter your prompt")

        if prompt:
            with st.chat_message("user"):
                st.markdown(prompt)
                self.chat.append_message(prompt, "user")

            with st.chat_message("assistant"):
                try:
                    response = st.write_stream(self.chat.response_generator())
                    self.chat.append_message(response, "assistant")
                except ResponseError as e:
                    st.write(e.error)

if __name__ == "__main__":
    chat = OllamaChat(st.session_state)
    ui = Ui(chat)
    ui.run()
