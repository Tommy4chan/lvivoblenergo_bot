from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from bot.utils import get_weekday, get_state_in_emoji
from bot.database.methods.select import is_user_notfication_enabled


def get_schedule_menu(user_id, selected_weekday):
    name_of_weekday_short = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Нд']
    
    user_notification_state = is_user_notfication_enabled(user_id)
    current_weekday = get_weekday()

    if current_weekday == selected_weekday:
        name_of_weekday_short[current_weekday] = f"{name_of_weekday_short[current_weekday]} {get_state_in_emoji(1)}"
    else:
        if user_notification_state:
            name_of_weekday_short[current_weekday] = f"{name_of_weekday_short[current_weekday]} {get_state_in_emoji(0)}"
        name_of_weekday_short[selected_weekday] = f"{name_of_weekday_short[selected_weekday]} {get_state_in_emoji(1)}"
    
    schedule_menu = InlineKeyboardMarkup(row_width=3)
    weekday_inline_keyboard_buttons = []

    for i in range(7):
        weekday_inline_keyboard_buttons.append(InlineKeyboardButton(text=name_of_weekday_short[i], callback_data=f'weekday_{i}'))

    schedule_menu.row(weekday_inline_keyboard_buttons[0], weekday_inline_keyboard_buttons[1], weekday_inline_keyboard_buttons[2])
    schedule_menu.row(weekday_inline_keyboard_buttons[3], weekday_inline_keyboard_buttons[4], weekday_inline_keyboard_buttons[5], weekday_inline_keyboard_buttons[6])
    schedule_menu.row(InlineKeyboardButton(text='Змінити групу', callback_data='change_group'))
    schedule_menu.row(InlineKeyboardButton(text=f'Сповіщення {get_state_in_emoji(user_notification_state)}', callback_data=f'notification_{user_notification_state}'), 
                    InlineKeyboardButton(text=f'Що це?', callback_data='what_is_notification'))
    schedule_menu.row(InlineKeyboardButton(text='Розробник', callback_data='developer'), InlineKeyboardButton(text='Донат', callback_data='donate'))
    return schedule_menu