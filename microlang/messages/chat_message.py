from pydantic import BaseModel
import tiktoken
class ChatMessage(BaseModel):
    value: str
    sender: str

    def __init__(self, value: str, sender: str) -> None:
        """Define a new chat message.

        Args:
            value (str): The role of the sender.
            sender (str): The contained string in the message.
        """
        super().__init__(value=value, sender=sender)
        
    def tokens(self, encoding:str = "cl100k_base") -> int:
        """A method to obtain the contained tokens in the ChatMessage.

        Args:
            encoding (str, optional): The encoding that the model uses. Defaults to "cl100k_base".

        Returns:
            int: The amount of tokens contained within the ChatMessage in the given encoding.
        """
        encoder = tiktoken.get_encoding(encoding)
        
        return len(encoder.encode(self.value))