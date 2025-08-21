# model_loader.py
# Description: Handles loading the Hugging Face model and tokenizer.

import os
import torch
from transformers import pipeline
from dotenv import load_dotenv
from huggingface_hub import login

def load_model():
    """
    Loads the Hugging Face text generation model and tokenizer.

    Logs into Hugging Face using a token from the .env file,
    then loads the specified model with the appropriate data type.

    Returns:
        A Hugging Face pipeline object for text generation.
    """
    # Load environment variables from .env file
    load_dotenv()
    
    # Login to Hugging Face Hub
    hf_token = os.getenv("hf-auth-login")
    if not hf_token:
        raise ValueError("Hugging Face token not found. Please set HF_AUTH_TOKEN in your .env file.")
    
    try:
        login(token=hf_token)
        print("Successfully logged into Hugging Face Hub.")
    except Exception as e:
        print(f"Error logging into Hugging Face Hub: {e}")
        return None

    # Initialize the text generation pipeline
    # Using a smaller, efficient model suitable for local execution.
    # torch.bfloat16 is used for faster inference on compatible hardware.
    print("Loading model... This may take a moment.")
    try:
        pipe = pipeline(
            "text-generation", 
            model="google/gemma-3-270m-it", 
            torch_dtype=torch.bfloat16,
            device_map="auto" # Automatically uses GPU if available
        )
        print("Model loaded successfully.")
        return pipe
    except Exception as e:
        print(f"Error loading model: {e}")
        return None
