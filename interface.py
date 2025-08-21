# interface.py
# Description: The main command-line interface for the chatbot.

from model_loader import load_model
from chat_memory import ChatMemory

def main():
    """
    Main function to run the chatbot CLI.
    """
    # 1. Load the model
    model_pipeline = load_model()
    if not model_pipeline:
        print("Failed to load the model. Exiting.")
        return

    # 2. Initialize chat memory
    # We'll remember the last 3 turns of conversation.
    memory = ChatMemory(window_size=3)
    
    print("\n--- Local Chatbot Initialized ---")
    print("Model: google/gemma-3-270m-it")
    print("Type '/history' to view conversation history.")
    print("Type '/exit' to end the conversation.")
    print("---------------------------------\n")

    # 3. Start the chat loop
    while True:
        try:
            # Get user input
            user_input = input("User: ")

            # Check for exit command
            if user_input.strip().lower() == '/exit':
                print("Bot: Exiting chatbot. Goodbye!")
                break
            

            if user_input.strip().lower() == '/history':
                print(f"{'-'*6}Conversation History:{'-'*6}")
                for i, msg in enumerate(memory.get_history(),1):
                    print(f"{i}. {msg['role']}: {msg['content']}")
                print(f"{'-'*6}End of History{'-'*6}\n")
                continue

            # Add user message to memory
            memory.add_message("user", user_input)
            
            # Get the current conversation history to use as context
            conversation_history = memory.get_history()
            
            # Generate a response from the model
            # max_new_tokens controls the length of the response.
            # The pipeline will automatically handle the conversation format.
            response = model_pipeline(
                conversation_history,
                max_new_tokens=150,
                do_sample=True,
                temperature=0.7,
            )
            
            # The pipeline returns the full conversation. We need the last message.
            bot_message = response[0]['generated_text'][-1]
            bot_response_content = bot_message['content']

            # Print the bot's response and add it to memory
            print(f"Bot: {bot_response_content}")
            memory.add_message("assistant", bot_response_content)

        except KeyboardInterrupt:
            print("\nBot: Exiting chatbot. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

if __name__ == "__main__":
    main()
