from pydantic import BaseModel
from datetime import datetime


class MessageBase(BaseModel):
    user: str
    text: str


class MessageCreate(MessageBase):
   pass


class Message(MessageBase):
    id: str
    date: datetime | str
