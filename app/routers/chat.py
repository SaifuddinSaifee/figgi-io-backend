from fastapi import APIRouter, HTTPException
from app.models.schemas import ChatRequest
from app.services.chat_service import ChatService
from fastapi.responses import StreamingResponse

router = APIRouter()
chat_service = ChatService()

@router.post("/chat")
async def create_chat(request: ChatRequest) -> StreamingResponse:
    try:
        return await chat_service.generate_streaming_response(
            messages=request.messages,
            model=request.model
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))