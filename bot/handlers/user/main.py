from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text

from bot.keyboards import KB_CONTINUE_REGISTRATION, KB_CHOOSE_GROUP, KB_POWEROFF_SCHEDULE, get_schedule_menu

from bot.utils import decode_callback_data, get_poweroff_schedule_text, get_weekday, rate_limit, telegram_chat_logging

from bot.database.methods.other import register_user
from bot.database.methods.update import update_user_group, update_user_notification_state


@telegram_chat_logging
async def __start(msg: Message):
    """
    This handler will be called when user sends `/start` or `/restart`
    command to launch or restart bot
    """
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await register_user(user_id, f'@{msg.from_user.username}, {msg.from_user.full_name}')
    await bot.send_message(user_id, "Привіт!\nЯ неофіційний бот, що буде показувати графік відключення електроенергії спираючись на публічні дані опубліковані Львівобленерго", reply_markup=KB_CONTINUE_REGISTRATION)


@rate_limit(limit=5, key='new_poweroff_schedule')
@telegram_chat_logging
async def __new_poweroff_schedule(msg: Message):
    """
    This handler will be called when user sends message
    with text "Графік відключень🕔" to send poweroff
    schedule
    """
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    weekday = get_weekday()

    await bot.send_message(user_id, await get_poweroff_schedule_text(user_id, weekday), reply_markup=await get_schedule_menu(user_id, weekday), parse_mode='Markdown')


@telegram_chat_logging
async def __change_group(query: CallbackQuery):
    """
    This query handler will be called when user change group
    """
    bot: Bot = query.bot
    user_id = query.from_user.id

    await bot.send_message(user_id, "Оберіть свою групу:", reply_markup=KB_CHOOSE_GROUP)
    await query.answer()


@telegram_chat_logging
async def __group_choosed(query: CallbackQuery):
    """
    This query handler will be called when group is choosed choosed
    """
    bot: Bot = query.bot
    user_id = query.from_user.id
    group_number = await decode_callback_data(query)

    await update_user_group(user_id, group_number)

    await bot.send_message(user_id, f"Ви обрали {group_number} групу", reply_markup=KB_POWEROFF_SCHEDULE)
    await __new_poweroff_schedule(query)
    await query.answer()


@telegram_chat_logging
async def __select_another_day(query: CallbackQuery):
    """
    This query handler will be called when user change day to another
    """
    user_id = query.from_user.id
    selected_weekday = await decode_callback_data(query)

    await query.message.edit_text(await get_poweroff_schedule_text(user_id, selected_weekday), reply_markup=await get_schedule_menu(user_id, selected_weekday), parse_mode='Markdown')
    await query.answer()


@telegram_chat_logging
async def __change_notification_state(query: CallbackQuery):
    """
    This query handler will be called when user change notification state
    """
    user_id = query.from_user.id
    weekday = get_weekday()
    
    await update_user_notification_state(user_id, await decode_callback_data(query))

    await query.message.edit_text(await get_poweroff_schedule_text(user_id, weekday), reply_markup=await get_schedule_menu(user_id, weekday), parse_mode='Markdown')
    await query.answer()


@telegram_chat_logging
async def __what_is_notification(query: CallbackQuery):
    """
    This query handler will be called when user click on "Що це?" button
    """
    bot: Bot = query.bot
    user_id = query.from_user.id

    await bot.send_message(user_id, f'Ви можете увімкнути сповіщення, щоб Бот кожен день відправляв Вам графік відключень в іншому випадку Вам самим доведеться змінювати день')
    await query.answer()


@telegram_chat_logging
async def __developer(query: CallbackQuery):
    """
    This query handler will be called when user click on "Розробник" button
    """
    bot: Bot = query.bot
    user_id = query.from_user.id

    await bot.send_message(user_id, f'Розробник цього бота Панурін Антон, студент Національного університету "Львівська Політехніка" 😎\nУ разі виникнення запитань, пропозицій, або проблем писати @Tommy4chan')
    await query.answer()


@telegram_chat_logging
async def __donate(query: CallbackQuery):
    """
    This query handler will be called when user click on "Донат" button
    """
    bot: Bot = query.bot
    user_id = query.from_user.id

    await bot.send_message(user_id, f'Для підтримки розробника та оплати хостингу Ви можете зробити донат: https://send.monobank.ua/jar/42BHbjmmq6')
    await query.answer()


def register_users_handlers(dp: Dispatcher):

    # Message handlers
    
    dp.register_message_handler(__start, commands=["start", "restart"])
    dp.register_message_handler(__new_poweroff_schedule, content_types=['text'], text="Графік відключень🕔")

    # Callback handlers

    dp.register_callback_query_handler(__change_group, text="change_group")
    dp.register_callback_query_handler(__group_choosed, Text(startswith='group_'))
    dp.register_callback_query_handler(__select_another_day, Text(startswith='weekday_'))
    dp.register_callback_query_handler(__change_notification_state, Text(startswith='notification_'))
    dp.register_callback_query_handler(__what_is_notification, Text(startswith='what_is_notification'))
    dp.register_callback_query_handler(__developer, Text(startswith='developer'))
    dp.register_callback_query_handler(__donate, Text(startswith='donate'))