#!/usr/bin/env python3
import requests
import json
import argparse
import sys

def check_ollama_running():
    """
    Check if Ollama is running by attempting to connect to its API.
    
    Returns:
        bool: True if Ollama is running, False otherwise
    """
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=2)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def chat_with_model(model_name, prompt):
    """
    Send a prompt to an Ollama model and get the response.
    
    Args:
        model_name (str): Name of the model to use (e.g., "llama3", "mistral", "phi")
        prompt (str): The prompt to send to the model
        
    Returns:
        str: The model's response
    """
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": model_name,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        result = response.json()
        return result["response"]
    except requests.exceptions.ConnectionError:
        return "ERROR: Could not connect to Ollama. Please make sure Ollama is installed and running."
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404 and "model not found" in response.text.lower():
            return f"ERROR: Model '{model_name}' not found. Try pulling it first with 'ollama pull {model_name}'."
        return f"ERROR: HTTP error occurred: {str(e)}"
    except requests.exceptions.RequestException as e:
        return f"ERROR: Request error occurred: {str(e)}"
    except KeyError:
        return "ERROR: Unexpected response format from Ollama API."
    except Exception as e:
        return f"ERROR: An unexpected error occurred: {str(e)}"

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Chat with Ollama models")
    parser.add_argument("--model", "-m", default="llama3", 
                        help="Model name (e.g., llama3, mistral, phi, dolphin, tinyllama)")
    parser.add_argument("--prompt", "-p", required=True, 
                        help="Prompt to send to the model")
    
    args = parser.parse_args()
    
    # Check if Ollama is running
    if not check_ollama_running():
        print("ERROR: Ollama is not running. Please start Ollama and try again.")
        print("\nInstallation instructions:")
        print("1. Download Ollama from https://ollama.com/download")
        print("2. Install and start the Ollama application")
        print("3. Run this script again")
        sys.exit(1)
    
    print(f"Prompt: {args.prompt}")
    print("\nThinking...\n")
    
    response = chat_with_model(args.model, args.prompt)
    
    # Check if the response starts with ERROR
    if response.startswith("ERROR:"):
        print(response)
        sys.exit(1)
    
    print(f"Response from {args.model}:\n{response}")

if __name__ == "__main__":
    main()