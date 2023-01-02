from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher.filters import Text

from bot.keyboards import KB_ADMIN_SEND_MESSAGE
from bot.utils.message import send_message_to_users
from bot.database.methods.select import get_all_users
from bot.database.methods.other import change_failsafe_state

from bot.utils import is_admin


@is_admin
async def __send_message_to_users(message: Message):
    """
    This handler will be called when user sends `/message`
    command to make bot send args of this message as global
    message for users
    """
    try:
        arguments = message.get_args()
    except:
        arguments = "Вкажи текст йолоп"
    await message.reply(arguments, reply_markup=KB_ADMIN_SEND_MESSAGE)


@is_admin
async def __number_of_users(message: Message):
    await message.reply(f"Кількість користувачів: {len(await get_all_users())}")


@is_admin
async def __failsafe(message: Message):
    await message.reply(await change_failsafe_state())


@is_admin
async def __send_message_to_all(query: CallbackQuery):
    """
    This query handler will be called to send message for all
    users by admin manually
    """
    bot: Bot = query.bot

    await send_message_to_users(bot, 1, query.message.text)

    await query.answer()


@is_admin
async def __send_message_to_users_with_notification(query: CallbackQuery):
    """
    This query handler will be called to send message for all
    users with enabled notification by admin manually
    """
    bot: Bot = query.bot

    await send_message_to_users(bot, 0, query.message.text)

    await query.answer()


def register_admin_handlers(dp: Dispatcher):

    # Message handlers
    
    dp.register_message_handler(__send_message_to_users, commands=["message"])
    dp.register_message_handler(__number_of_users, commands=["users"])
    dp.register_message_handler(__failsafe, commands=["failsafe"])

    # Callback handlers

    dp.register_callback_query_handler(__send_message_to_all, text="send_all")
    dp.register_callback_query_handler(__send_message_to_users_with_notification, text="send_to_users_with_notification")
