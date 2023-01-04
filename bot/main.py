import os
import asyncio
import aioschedule

from aiogram import Bot, Dispatcher, executor
from aiogram.utils.executor import start_webhook
import bot.middleware as middleware
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from bot.handlers import register_all_handlers
from bot.database.methods.select import get_bot_notification_time
from bot.utils.message import send_new_schedule

from dotenv import load_dotenv # For local use only

load_dotenv() # For local use only

BOT_TOKEN = os.getenv('BOT_TOKEN')
#APP_NAME = os.getenv('APP_NAME')
#
#WEBHOOK_HOST = f'https://{APP_NAME}.ondigitalocean.app'
#WEBHOOK_PATH = f'/webhook/{BOT_TOKEN}'
#WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
#
#WEBAPP_HOST = '0.0.0.0'
#WEBAPP_PORT = os.getenv('PORT', default=8000)

async def __on_start_up(dp: Dispatcher):
    #await dp.bot.set_webhook(WEBHOOK_URL)
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
    
    #start_webhook(
    #    dispatcher=dp,
    #    webhook_path=WEBHOOK_PATH,
    #    on_startup=__on_start_up,
    #    skip_updates=True,
    #    host=WEBAPP_HOST,
    #    port=WEBAPP_PORT,
    #)
    
    executor.start_polling(dp, skip_updates=True, on_startup=__on_start_up)