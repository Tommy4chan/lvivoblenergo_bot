from typing import Final
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


KB_POWEROFF_SCHEDULE: Final = ReplyKeyboardMarkup(1, resize_keyboard=True)
KB_POWEROFF_SCHEDULE.add(KeyboardButton(text="Графік відключень🕔"))