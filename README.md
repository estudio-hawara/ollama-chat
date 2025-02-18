# Local chat with Ollama and Streamlit

## Install

To install this application you'll need Git, Python and Poetry installed in your computer. Once you have them, clone the repository:

```bash
git clone https://github.com/estudio-hawara/ollama-chat.git
```

and install the dependencies:

```bash
poetry install
```

## Configure

The default Ollama settings are the ones defined in `env.default`:

```bash
OLLAMA_MODEL=deepseek-r1:7b
OLLAMA_SERVER=localhost
OLLAMA_PORT=11434
```

If you want to define your own values, create a `.env` file with the variables and values that you want to customize:

```bash
OLLAMA_MODEL=deepseek-r1:14b
```

## Open a shell

Once the application has been installed, you can start working with it. To do so, first start a Poetry shell by running:

```bash
poetry shell
```

Now you can run any of the commands below.

## Run the chat

To run the chat, after opening a shell, run:

```bash
python -m streamlit run ollama_chat/ui.py
```

This should open a service at port 8501:

```
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.1:8501
```

## Test

This application is supported by unit tests. To execute them, run:

```bash
poetry run pytest
```
