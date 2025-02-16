from streamlit.testing.v1 import AppTest

def app():
    import streamlit as st
    from ollama_chat.chat.chat_base import ChatBase
    from ollama_chat.ui import Ui

    chat = ChatBase(st.session_state)
    ui = Ui(chat)
    ui.run()

def test_app_runs():
    at = AppTest.from_function(app)
    at.run()
    assert not at.exception

def test_messages_are_appended():
    at = AppTest.from_function(app)
    at.run()
    at.chat_input[0].set_value("What's a word?")
    at.chat_input[0].run()
    assert len(at.chat_message) == 2
    assert not at.exception
