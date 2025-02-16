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
