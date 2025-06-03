# Ollama Chat CLI

A lightweight Python command-line interface for interacting with Ollama's local large language models. This tool allows you to quickly send prompts to any Ollama model from your terminal without needing to use the web interface.

![Ollama Logo](https://ollama.com/public/ollama.png)

## Features

- Simple command-line interface for Ollama models
- Support for all Ollama models (llama3, mistral, phi, etc.)
- Non-streaming mode for complete responses
- Helpful error messages when Ollama is not running
- Windows batch file for easier usage
- Minimal dependencies (only requires the `requests` library)
- Easy to extend and customize

## Prerequisites

- Python 3.6 or higher
- Ollama installed and running locally ([Install Ollama](https://ollama.com/download))
- `requests` Python library

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/lokeshpanthangi/ollama-t1.git
   cd ollama-t1
   ```

2. Install the required Python library:
   ```bash
   pip install requests
   ```

3. Make sure Ollama is installed and running on your machine.
   - You can verify Ollama is running by visiting http://localhost:11434 in your browser
   - Or by running `curl http://localhost:11434/api/tags` in your terminal

## Usage

### Python Script

Run the script with the following command:

```bash
python ollama_chat.py --model MODEL_NAME --prompt "Your prompt here"
```

Or using the short form:

```bash
python ollama_chat.py -m MODEL_NAME -p "Your prompt here"
```

### Windows Batch File (Easier Method)

On Windows, you can use the included batch file for a simpler interface:

```bash
chat.bat "Your prompt here" [model_name]
```

If model_name is not specified, llama3 will be used by default.

### Examples

```bash
python ollama_chat.py --model llama3 --prompt "Explain quantum computing in simple terms"
```

```bash
python ollama_chat.py -m mistral -p "Write a short poem about AI"
```

```bash
chat.bat "Tell me a joke" phi
```

### Available Models

You can use any model that you have pulled in Ollama, such as:
- llama3
- mistral
- phi
- dolphin
- tinyllama
- gemma
- codellama
- llava (for multimodal capabilities)

To see available models in Ollama, run:
```bash
ollama list
```

To pull a new model:
```bash
ollama pull MODEL_NAME
```

## Error Handling

The script includes improved error handling to help you troubleshoot common issues:

- If Ollama is not running, you'll get clear instructions on how to install and start it
- If a model is not found, you'll get instructions on how to pull it
- Other API errors are also handled with descriptive messages

## How It Works

The script makes HTTP requests to the Ollama API running locally on port 11434. It sends your prompt to the specified model and returns the response.

## Customization

You can modify the script to add more features such as:
- Streaming responses
- Conversation history
- Model parameter adjustments (temperature, top_p, etc.)
- Output formatting options

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [Ollama](https://ollama.com) for making local LLMs accessible
- All contributors to this project