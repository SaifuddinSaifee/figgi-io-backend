from pydantic import BaseModel
from typing import List, Literal, Optional, Union

class Message(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]
    model: str = "qwen2.5:3b"

class ChatResponse(BaseModel):
    role: Literal["assistant"]
    content: str