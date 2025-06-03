#!/usr/bin/env python3
import requests
import json
import argparse

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
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description="Chat with Ollama models")
    parser.add_argument("--model", "-m", default="llama3", 
                        help="Model name (e.g., llama3, mistral, phi, dolphin, tinyllama)")
    parser.add_argument("--prompt", "-p", required=True, 
                        help="Prompt to send to the model")
    
    args = parser.parse_args()
    
    print(f"Prompt: {args.prompt}")
    print("\nThinking...\n")
    
    response = chat_with_model(args.model, args.prompt)
    
    print(f"Response from {args.model}:\n{response}")

if __name__ == "__main__":
    main() 