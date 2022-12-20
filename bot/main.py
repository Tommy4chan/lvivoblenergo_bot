import os
import asyncio
import aioschedule

from aiogram import Bot, Dispatcher, executor
import bot.middleware as middleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.handlers import register_all_handlers
from bot.database.methods.select import get_bot_notification_time
from bot.utils.message import send_new_schedule

from dotenv import load_dotenv # For local use only

load_dotenv() # For local use only

BOT_TOKEN = os.getenv('BOT_TOKEN')


async def __on_start_up(dp: Dispatcher):
    register_all_handlers(dp)
    middleware.setup(dp)
    asyncio.create_task(scheduler(dp))


async def scheduler(dp: Dispatcher):
    aioschedule.every().day.at(await get_bot_notification_time()).do(send_new_schedule, dp.bot)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


def start_bot():
    
    # Initializing bot and dispatcher
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)
    