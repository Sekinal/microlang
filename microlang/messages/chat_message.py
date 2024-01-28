from pydantic import BaseModel
import tiktoken
class ChatMessage(BaseModel):
    value: str
    sender: str
    encoding: str = "cl100k_base"
    tokens: int = 0

    def __init__(self, value: str, sender: str, encoding: str = encoding) -> None:
        """Define a new chat message.

        Args:
            value (str): The role of the sender.
            sender (str): The contained string in the message.
            encoding_val (str, optional): The encoding to be used for the message. Defaults to "cl100k_base".
        """
        super().__init__(value=value, sender=sender, encoding=encoding)
        self.tokens = self.get_tokens()
        
    def get_tokens(self) -> int:
        """A method to calculate the amount of tokens contained in the parent ChatMessage.
        
        Returns:
            int: The amount of tokens contained in the parent ChatMessage.
        """
        encoder = tiktoken.get_encoding(self.encoding)
        
        return len(encoder.encode(self.value))