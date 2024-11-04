# app/services/chat_service.py
from openai import OpenAI
from fastapi.responses import StreamingResponse
import json
from typing import List
from app.models.schemas import Message
from app.config import settings


class ChatService:
    def __init__(self):
        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY,
            base_url="http://localhost:11434/v1"
        )

    def create_chat_completion(self, messages: List[Message], model: str):
        """Create a chat completion with streaming"""
        return self.client.chat.completions.create(
            model=model,
            messages=[{"role": msg.role, "content": msg.content} for msg in messages],
            stream=True
        )

    async def generate_streaming_response(self, messages: List[Message], model: str):
        try:
            completion = self.create_chat_completion(messages, model)

            async def event_generator():
                for chunk in completion:
                    if content := chunk.choices[0].delta.content:
                        yield f"data: {json.dumps({'content': content})}\n\n"
                yield "data: [DONE]\n\n"

            return StreamingResponse(
                event_generator(),
                media_type="text/event-stream"
            )

        except Exception as e:
            raise Exception(f"Error generating chat response: {str(e)}")