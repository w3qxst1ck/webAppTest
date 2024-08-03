from fastapi import APIRouter
from fastapi_pagination import Page, paginate

from ..models.messages import MessageCreate, Message
from ..services import messages


router = APIRouter(
    prefix='/messages'
)


@router.get("/", response_model=Page[Message])
async def get_messages():
    return paginate(await messages.get_messages_from_db())


@router.post("/", response_model=Message)
async def create_message(message_data: MessageCreate):
    new_message = await messages.create_message_in_db(message_data)
    return new_message


@router.get("/{message_id}", response_model=Message | None)
async def get_message(message_id: str):
    message = await messages.get_message_from_db_by_id(message_id)
    return message
