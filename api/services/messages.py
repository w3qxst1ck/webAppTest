import datetime

from bson import ObjectId

from ..models.messages import MessageCreate, Message
from ..database import database


async def get_messages_from_db() -> list[Message]:
    cursor = database.test_collection.find({}).sort("date", -1)

    res = []

    for item in await cursor.to_list(length=None):
        message = Message(
            id=str(item["_id"]),
            user=item["user"],
            text=item["text"],
            date=datetime.datetime.strftime(datetime.datetime.fromtimestamp(item["date"]), '%d.%m.%Y, %H:%M:%S'),
        )
        res.append(message)

    return res


async def create_message_in_db(message: MessageCreate) -> Message:
    inserted_message = {
        "user": message.user,
        "text": message.text,
        "date": datetime.datetime.now().timestamp()
    }
    result = await database.test_collection.insert_one(inserted_message)

    new_message = Message(
        id=str(result.inserted_id),
        user=inserted_message["user"],
        text=inserted_message["text"],
        date=inserted_message["date"]
    )

    return new_message


async def get_message_from_db_by_id(id: str) -> Message:
    result = database.test_collection.find({"_id": ObjectId(id)})

    for item in await result.to_list(length=1):
        message = Message(
            id=str(item["_id"]),
            user=item["user"],
            text=item["text"],
            date=datetime.datetime.strftime(datetime.datetime.fromtimestamp(item["date"]), '%d.%m.%Y, %H:%M:%S'),
        )

        return message
