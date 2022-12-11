import os
from contextlib import suppress

from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.exceptions import ChatNotFound, BotBlocked

from bot.handlers import register_all_handlers

from dotenv import load_dotenv # For local user only

load_dotenv() # For local user only

BOT_TOKEN = os.getenv('BOT_TOKEN')


async def __on_start_up(dp: Dispatcher):
    register_all_handlers(dp)


def start_bot():
    
    # Initializing bot and dispatcher

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
    