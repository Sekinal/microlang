from typing import List

from pydantic import BaseModel

from ..messages import ChatMessage


class ConversationMemory(BaseModel):
    messages: List[ChatMessage] = []

    def __init__(self, messages: List[ChatMessage] = messages) -> None:
        super().__init__(messages=messages)

    def add_message(self, message: ChatMessage) -> None:
        """
        Adds a ChatMessage to the list of messages.

        Args:
            self: The instance of the ConversationMemory class.
            message (ChatMessage): The ChatMessage object to be added.

        Returns:
            None

        Examples:
        >>> memory = ConversationMemory()
        >>> message = ChatMessage(value = "Hello", sender="Alice")
        >>> memory.add_message(message)
        """

        self.messages.append(message)

    def delete_message(self, to_remove: int or str) -> None:
        """
        Deletes a message from the conversation memory.

        Args:
            to_remove (int or str): The index or content of the message to be removed.
            If a string is given, it deletes the first encounter of the string from right to left.

        Returns:
            None

        Raises:
            None

        Examples:
            By using index,
            >>> memory = ConversationMemory()
            >>> message = ChatMessage(value = "Hello", sender="Alice")
            >>> memory.add_message(message)
            >>> memory.delete_message(0)
            By using string,
            >>> memory.delete_message("Hello")
        """

        if isinstance(to_remove, int):
            del self.messages[to_remove]
        elif isinstance(to_remove, str):
            self.messages = self.messages[::-1].remove(to_remove)

    def clear_conversation(self) -> None:
        self.messages.clear()
