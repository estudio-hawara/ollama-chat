class ChatBase:
    def __init__(self, session_state):
        self.session = session_state

    def get_messages(self) -> list:
        if not "messages" in self.session:
            self.session["messages"] = []
        return self.session["messages"]

    def get_model(self) -> str:
        if not "model" in self.session:
            self.session["model"] = ""
        return self.session["model"]

    def append_message(self, message: str, role: str):
        messages = self.get_messages()
        messages.append({
            "role": role,
            "content": message,
        })

    def response_generator(self):
        for message in self.get_messages():
            yield message["content"]
