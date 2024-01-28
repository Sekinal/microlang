import pytest
import microlang

def test_ChatMessage():
    message = microlang.messages.ChatMessage(role = "gpt", value = "hey")
    
    assert message.value == "hey"

def test_tokens():
    message = microlang.messages.ChatMessage(role = "gpt", value = "hey")
    
    assert message.value == "hey"