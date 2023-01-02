import logging
import os
import asyncio
from aiogram import Bot

from bot.utils.main import get_weekday, get_poweroff_schedule_text
from bot.database.methods.select import get_all_users_with_enabled_notification, get_all_users, is_failsafe_enabled
from bot.keyboards import get_schedule_menu

from dotenv import load_dotenv # For local use only

load_dotenv() # For local use only

ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')


async def send_new_schedule(bot: Bot):
    if not await is_failsafe_enabled():
        weekday = get_weekday()
        for user_id in await get_all_users_with_enabled_notification():
            await asyncio.sleep(0.07)
            try:
                await bot.send_message(user_id[0], await get_poweroff_schedule_text(user_id[0], weekday), reply_markup=await get_schedule_menu(user_id[0], weekday), parse_mode='Markdown')
            except Exception as e:
                logging.warning(f"User_id: {user_id[0]}, {e}")
                pass
        await bot.send_message(ADMIN_CHAT_ID, "Оновлений розклад доставлений усім користувачам")
    else:
        await bot.send_message(ADMIN_CHAT_ID, "Failsafe є включений")
    

async def send_message_to_users(bot, is_all_user_message, message_text):
    if not await is_failsafe_enabled():
        weekday = get_weekday()
        for user_id in await get_all_users() if is_all_user_message else await get_all_users_with_enabled_notification():
            await asyncio.sleep(0.07)
            try:
                await bot.send_message(user_id[0], await get_poweroff_schedule_text(user_id[0], weekday), reply_markup=await get_schedule_menu(user_id[0], weekday), parse_mode='Markdown')
                await bot.send_message(user_id[0], message_text, parse_mode='Markdown')
            except Exception as e:
                logging.warning(f"User_id: {user_id[0]}, {e}")
                pass
        await bot.send_message(ADMIN_CHAT_ID, "Повідомлення доставлене усім користувачам")
    else:
        await bot.send_message(ADMIN_CHAT_ID, "Failsafe є включений")