from ollama_chat.settings import Settings

def test_default_settings():
    settings = Settings()
    assert type(settings.ollama_model) == str
    assert type(settings.ollama_server) == str
    assert type(settings.ollama_port) == str
