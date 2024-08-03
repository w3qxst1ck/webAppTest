import os
import dotenv

dotenv.load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
DOMEN = os.getenv("DOMEN")
PAGE_SIZE = 5