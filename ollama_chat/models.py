from ollama import ListResponse, list

def list_models():
    try:
        response: ListResponse = list()
        return [item.model for item in response.models]
    except:
        return []
