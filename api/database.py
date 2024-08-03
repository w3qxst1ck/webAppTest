from motor.motor_asyncio import AsyncIOMotorClient
from api.config import DATABASE_URL

client = AsyncIOMotorClient(DATABASE_URL)
database = client["test_database"]



