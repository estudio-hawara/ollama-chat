from dotenv import dotenv_values

class Settings:
    def __init__(self):
        config = {
            **dotenv_values("env.default"),
            **dotenv_values(".env"),
        }

        self.ollama_model = config["OLLAMA_MODEL"]
        self.ollama_server = config["OLLAMA_SERVER"]
        self.ollama_port = config["OLLAMA_PORT"]