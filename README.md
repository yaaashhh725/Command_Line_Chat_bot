# Command Line Chat Bot

A simple command-line chatbot powered by Hugging Face Transformers, designed for local use. It maintains a short conversation history and supports basic commands for interaction.

## Features
- Local inference using `google/gemma-3-270m-it` model
- Remembers last 3 turns of conversation
- View conversation history
- Simple CLI interface

## Setup Instructions

### 1. Clone the Repository
```powershell
git clone https://github.com/yaaashhh725/Command_Line_Chat_bot.git  
cd Command_Line_Chat_bot
```

### 2. Python Environment and Dependency Installation (using `uv`)
This project uses [`uv`](https://docs.astral.sh/uv/) for fast Python package management and virtual environment creation. It relies on `pyproject.toml` for dependencies and `uv.lock` for locked versions.

Ensure you have Python 3.8+ and `uv` installed. Then, create a virtual environment and install dependencies directly using `uv`:
```bash
uv sync
```
*Note: `uv sync` will also create and manage a virtual environment by default (usually in `.venv`). If you want it to use the `venv` folder you created, you might need to adjust the command or environment variables accordingly, or just use `uv pip install .` within your activated `venv`.*

*Alternatively, you can manually create virtual enviornment and install the dependencies*
```powershell
# Create and activate a virtual environment named 'venv'
uv venv venv
# On Windows (PowerShell)
.\venv\Scripts\Activate.ps1
# On macOS/Linux
# source venv/bin/activate

# Install dependencies using uv (automatically reads pyproject.toml)
uv pip install .
```




### 3. Hugging Face Authentication
Create a `.env` file in the project root with your Hugging Face token:
```
hf-auth-login=YOUR_HUGGINGFACE_TOKEN
```
Get your token from [Hugging Face Settings](https://huggingface.co/settings/tokens).

## How to Run
Run the chatbot from the command line (ensure the virtual environment created/used by `uv` is active):
```powershell
uv run interface.py
```

## Usage Example
```
--- Local Chatbot Initialized ---
Model: google/gemma-3-270m-it
Type '/history' to view conversation history.
Type '/exit' to end the conversation.
---------------------------------

User: Hello!
Bot: Hi there! How can I assist you today?

User: What's the weather like?
Bot: I'm a local chatbot and don't have access to real-time data, but I can help with general questions!

User: /history
------Conversation History:------
1. user: Hello!
2. assistant: Hi there! How can I assist you today?
3. user: What's the weather like?
4. assistant: I'm a local chatbot and don't have access to real-time data, but I can help with general questions!
------End of History------

User: /exit
Bot: Exiting chatbot. Goodbye!
```

## Troubleshooting
- **Model loading issues:** Ensure your Hugging Face token is valid and you have internet access for the first run.
- **CUDA/GPU errors:** The model will use GPU if available, otherwise defaults to CPU.
- **Missing dependencies:** Double-check your Python environment and installed packages using `uv pip list`.


