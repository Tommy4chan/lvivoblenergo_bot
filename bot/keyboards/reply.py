from typing import Final
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

KB_POWEROFF_SCHEDULE: Final = ReplyKeyboardMarkup(1)
KB_POWEROFF_SCHEDULE.add(KeyboardButton(text="Графік відключень🕔"))