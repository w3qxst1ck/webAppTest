import asyncio
from asyncio.log import logger

import aiogram as io
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, BotCommandScopeDefault
from config import BOT_TOKEN
from router import router


async def set_commands(bot: io.Bot):
    """Перечень команд для бота"""
    commands = [
        BotCommand(command="start", description="Запуск бота"),
        BotCommand(command="help", description="Справочная информация"),
        BotCommand(command="messages", description="Все сообщения"),
        BotCommand(command="create", description="Создать сообщение"),
        BotCommand(command="find", description="Получить сообщение по ID"),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def start_bot() -> None:
    """Starting telegram bot"""
    bot = io.Bot(BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    storage = MemoryStorage()
    dispatcher = io.Dispatcher(storage=storage)
    await set_commands(bot)

    dispatcher.include_routers(router)

    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logger.info("Starting bot...")
    asyncio.run(start_bot())