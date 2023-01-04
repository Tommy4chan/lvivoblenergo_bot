from datetime import datetime
import pytz
import os
import logging

from aiogram import Bot
from bot.database.methods.select import is_user_notfication_enabled, get_user_group, is_user_admin

from dotenv import load_dotenv # For local use only

load_dotenv() # For local use only

ADMIN_CHAT_ID = os.getenv('ADMIN_CHAT_ID')


async def decode_callback_data(callback):
    return int(callback.data.split('_')[1])


def is_admin(func):
    async def inner_function(*args):
        user_id = args[0].from_user.id
        if await is_user_admin(user_id):
            await func(*args)
    return inner_function


def telegram_chat_logging(func):
    async def inner_function(*args):
        log_message = ""
        try:
            log_message = "Function name: " + str(func.__name__)
            await func(*args)
        except Exception as e:
            log_message += "\nError: " + str(e)
            pass
        callback_query = args[0]
        try:
            await callback_query.bot.send_message(ADMIN_CHAT_ID, f"User: {callback_query.from_user.full_name}\nUsername: @{callback_query.from_user.username}\n{log_message}")
        except Exception as e:
            logging.warning(e)
            pass
    return inner_function


async def get_poweroff_schedule_text(user_id, selected_weekday):
    poweroff_schedule = [[[0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2]],
                        [[1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0]],
                        [[2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1], [0, 1, 2, 0, 1, 2], [1, 2, 0, 1, 2, 0], [2, 0, 1, 2, 0, 1]]]
    poweroff_schedule_time = ['1:00-5:00', '5:00-9:00', '9:00-13:00', '13:00-17:00', '17:00-21:00', '21:00-1:00']
    name_of_weekday = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', "П'ятниця", 'Субота', 'Неділя']

    weekday_name = name_of_weekday[selected_weekday]
    user_group = await get_user_group(user_id) - 1
    poweroff_schedule_text = ''
    for i in range(6):
        poweroff_schedule_text += '\n'
        poweroff_schedule_text += f'*{poweroff_schedule_time[i]}*'
        if poweroff_schedule[user_group][selected_weekday][i] == 0:
            poweroff_schedule_text += ' - Електроенергія ❌'
        elif poweroff_schedule[user_group][selected_weekday][i] == 1:
            poweroff_schedule_text += ' - Електроенергія ✅'
        else:
            poweroff_schedule_text += ' - Електроенергія ⚠️'
    poweroff_schedule_text = f'Ваша група - {user_group + 1}\nВибрано: {weekday_name}\n' + poweroff_schedule_text
    if not await is_user_notfication_enabled(user_id):
        return poweroff_schedule_text
    return f'Сьогодні: {name_of_weekday[get_weekday()]}, {poweroff_schedule_text}'


def get_weekday():
    dt = datetime.now(pytz.timezone('Europe/Kiev'))
    return dt.weekday()


def get_state_in_emoji(state):
    state_in_emoji = ["☑️", "✅"]
    return state_in_emoji[state]