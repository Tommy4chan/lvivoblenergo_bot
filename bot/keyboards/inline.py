from typing import Final
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

KB_CONTINUE_REGISTRATION: Final = InlineKeyboardMarkup(1)
KB_CONTINUE_REGISTRATION.add(
    InlineKeyboardButton("Продовжити", callback_data="change_group")
)

KB_CHOOSE_GROUP: Final = InlineKeyboardMarkup(row_width=3)
KB_CHOOSE_GROUP.add(InlineKeyboardButton(text='Група 1', callback_data='group_1'),
          InlineKeyboardButton(text='Група 2', callback_data='group_2'),
          InlineKeyboardButton(text='Група 3', callback_data='group_3'),
          InlineKeyboardButton(text='Дізнатись групу', url='https://poweroff.loe.lviv.ua/gav_city3'))