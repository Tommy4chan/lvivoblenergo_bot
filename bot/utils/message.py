from aiogram import Bot

from bot.utils.main import get_weekday, get_poweroff_schedule_text
from bot.database.methods.select import get_all_users_with_enabled_notification
from bot.keyboards import get_schedule_menu

async def send_new_schedule(bot: Bot):
    weekday = get_weekday()
    for user_id in await get_all_users_with_enabled_notification():
        await bot.send_message(user_id[0], await get_poweroff_schedule_text(user_id[0], weekday), reply_markup=await get_schedule_menu(user_id[0], weekday), parse_mode='Markdown')