from pydantic import BaseModel
import tiktoken
class ChatMessage(BaseModel):
    value: str
    sender: str
    tokens: int = 0

    def __init__(self, value: str, sender: str) -> None:
        """Define a new chat message.

        Args:
            value (str): The role of the sender.
            sender (str): The contained string in the message.
        """
        super().__init__(value=value, sender=sender)
        
    def tokens(self, encoding:str = "cl100k_base") -> int:
        """A method to calculate the amount of tokens contained in the parent ChatMessage.
        
        Returns:
            int: The amount of tokens contained in the parent ChatMessage.
            encoding (str, optional): The encoding to be used for the message. Defaults to "cl100k_base".
        """
        encoder = tiktoken.get_encoding(encoding)
        
        return len(encoder.encode(self.value))