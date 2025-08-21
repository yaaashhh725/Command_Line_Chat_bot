from collections import deque

class ChatMemory:
    """
    A class to manage and store conversation history with a sliding window.
    """
    def __init__(self, window_size: int = 3):
        """
        Initializes the ChatMemory.

        Args:
            window_size (int): The number of conversation turns (user + bot) to remember.
        """
        if window_size < 1:
            raise ValueError("Window size must be at least 1.")
        # We store pairs of (user, bot) messages, so the deque size is 2 * window_size
        self.window_size = window_size * 2 
        self.history = deque(maxlen=self.window_size)

    def add_message(self, role: str, content: str):
        """
        Adds a new message to the conversation history.

        Args:
            role (str): The role of the speaker ('user' or 'assistant').
            content (str): The message content.
        """
        # The deque will automatically handle the sliding window by discarding
        # the oldest messages when the maximum length is reached.
        self.history.append({"role": role, "content": content})

    def get_history(self) -> list:
        """
        Retrieves the current conversation history within the window.

        Returns:
            list: A list of message dictionaries, formatted for the HF pipeline.
        """
        return list(self.history)

    def clear(self):
        """
        Clears the entire conversation history.
        """
        self.history.clear()
        print("Memory cleared.")
