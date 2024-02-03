from typing import List

from pydantic import BaseModel

from ..messages import ChatMessage


class ConversationMemory(BaseModel):
    messages: List[ChatMessage] = []
    tokens: int = 0

    def __init__(self, messages: List[ChatMessage] = messages, tokens: int = tokens) -> None:
        super().__init__(messages=messages, tokens = tokens)

    def add_message(self, message: ChatMessage) -> None:
        """Adds a ChatMessage to the list of messages.

        Args:
            message (ChatMessage): The ChatMessage to be added.
        """

        self.messages.append(message)
        self.tokens += message.tokens

    def delete_message(self, to_remove: int) -> None:
        """Deletes a ChatMessage from the list of messages.

        Args:
            to_remove (int): The index of the ChatMessage to remove.
        """
        
        self.tokens -= self.messages[to_remove].tokens
        del self.messages[to_remove]

    def clear_conversation(self) -> None:
        """Clears the conversation memory from all ChatMessages.
        """
        
        self.messages.clear()
