# Ollama Chat Script

A simple Python script to interact with Ollama models programmatically.

## Requirements
- Python 3.6+
- Ollama installed and running locally
- `requests` library

## Installation

1. Install the required Python library:
```
pip install requests
```

2. Make sure Ollama is installed and running on your machine.

## Usage

Run the script with the following command:

```
python ollama_chat.py --model MODEL_NAME --prompt "Your prompt here"
```

Or using the short form:

```
python ollama_chat.py -m MODEL_NAME -p "Your prompt here"
```

### Examples

```
python ollama_chat.py --model llama3 --prompt "Explain quantum computing in simple terms"
```

```
python ollama_chat.py -m mistral -p "Write a short poem about AI"
```

### Available Models

You can use any model that you have pulled in Ollama, such as:
- llama3
- mistral
- phi
- dolphin
- tinyllama

To see available models in Ollama, run:
```
ollama list
```

To pull a new model:
```
ollama pull MODEL_NAME
``` 