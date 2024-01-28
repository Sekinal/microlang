import tiktoken
import microlang

encoder = tiktoken.get_encoding("cl100k_base")
def test_ChatMessage_1():
    message = microlang.messages.ChatMessage(role = "gpt", value = "hey")
    
    assert message.role == "gpt" and message.value == "hey"

def test_ChatMessage_2():
    message = microlang.messages.ChatMessage(role = "user", value = "hey")
    
    assert message.role == "user" and message.value == "hey"
    
def test_tokens():
    msg_string = "Hey, how are you today?"
    message = microlang.messages.ChatMessage(role = "user", value = msg_string)
    
    assert len(encoder.encode(msg_string)) == message.get_tokens()