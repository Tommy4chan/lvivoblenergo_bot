from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text

from bot.keyboards import KB_CONTINUE_REGISTRATION, KB_CHOOSE_GROUP, KB_POWEROFF_SCHEDULE, get_schedule_menu

from bot.utils import decode_callback_data, get_poweroff_schedule_text, get_weekday

from bot.database.methods.other import register_user
from bot.database.methods.update import update_user_group

async def __start(msg: Message):
    """
    This handler will be called when user sends `/start` or `/restart`
    command to launch or restart bot
    """
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    register_user(user_id, f'@{msg.from_user.username}, {msg.from_user.full_name}')
    await bot.send_message(user_id, "Привіт!\nЯ неофіційний бот, що буде показувати графік відключення електроенергії спираючись на публічні дані опубліковані Львівобленерго", reply_markup=KB_CONTINUE_REGISTRATION)


async def __new_poweroff_schedule(msg: Message):
    """
    This handler will be called when user sends message
    with text "Графік відключень🕔" to send poweroff
    schedule
    """
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    weekday = get_weekday()

    await bot.send_message(user_id, get_poweroff_schedule_text(user_id, weekday), reply_markup=get_schedule_menu(user_id, weekday), parse_mode='Markdown')


async def __change_group(query: CallbackQuery):
    """
    This query handler will be called when user change group
    """
    bot: Bot = query.bot
    user_id = query.from_user.id

    await bot.send_message(user_id, "Оберіть свою групу:", reply_markup=KB_CHOOSE_GROUP)
    await query.answer()


async def __group_choosed(query: CallbackQuery):
    """
    This query handler will be called when group is choosed choosed
    """
    bot: Bot = query.bot
    user_id = query.from_user.id
    group_number = decode_callback_data(query)

    update_user_group(user_id, group_number)

    await bot.send_message(user_id, f"Ви обрали {group_number} групу", reply_markup=KB_POWEROFF_SCHEDULE)
    await __new_poweroff_schedule(query)
    await query.answer()

async def __select_another_day(query: CallbackQuery):
    """
    This query handler will be called when user change day to another
    """
    user_id = query.from_user.id
    selected_weekday = decode_callback_data(query)

    await query.message.edit_text(get_poweroff_schedule_text(user_id, selected_weekday), reply_markup=get_schedule_menu(user_id, selected_weekday), parse_mode='Markdown')
    await query.answer()

def register_users_handlers(dp: Dispatcher):

    # Message handlers
    
    dp.register_message_handler(__start, commands=["start", "restart"])
    dp.register_message_handler(__new_poweroff_schedule, content_types=['text'], text="Графік відключень🕔")

    # Callback handlers

    dp.register_callback_query_handler(__change_group, text="change_group")
    dp.register_callback_query_handler(__group_choosed, Text(startswith='group_'))
    dp.register_callback_query_handler(__select_another_day, Text(startswith='weekday_'))

