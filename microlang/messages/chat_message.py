from pydantic import BaseModel
import tiktoken

class ChatMessage(BaseModel):

    role: str
    value: str
    
    def __init__(self, role: str, value: str) -> None:
        """Define a new chat message.

        Args:
            role (str): The role of the sender.
            value (str): The contained string in the message.
        """
        super().__init__(role = role, value = value)
        
    def get_tokens(self, encoding: str = "cl100k_base") -> int:
        """A method to calculate the amount of tokens contained in the parent ChatMessage.

        Args:
            encoding (str, optional): The tiktoken supported encoding of the used model. Defaults to "cl100k_base".

        Returns:
            int: The amount of tokens contained in the parent ChatMessage.
        """
        encoder = tiktoken.get_encoding(encoding)
        
        return len(encoder.encode(self.value))