import ollama
from .chat_base import ChatBase

class OllamaChat(ChatBase):
    def __init__(self, session_state):
        self.session = session_state

    def append_message(self, message: str, role: str):
        messages = self.get_messages()
        messages.append({
            "role": role,
            "content": message,
        })

    def response_generator(self):
        response = ollama.chat(
            model=self.get_model(),
            messages=self.get_messages(),
            stream=True,
        )

        for chunk in response:
            yield chunk["message"]["content"]
