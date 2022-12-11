from aiogram import Dispatcher, Bot
from aiogram.types import Message, CallbackQuery

from bot.keyboards import KB_CONTINUE_REGISTRATION, KB_CHOOSE_GROUP

async def __start(msg: Message):
    """
    This handler will be called when user sends `/start` or `/restart` command
    to launch or restart bot
    """
    bot: Bot = msg.bot
    user_id = msg.from_user.id
    await bot.send_message(user_id, "Привіт!\nЯ неофіційний бот, що буде показувати графік відключення електроенергії спираючись на публічні дані опубліковані Львівобленерго", reply_markup=KB_CONTINUE_REGISTRATION)


async def __choose_group(query: CallbackQuery):
    """
    This query handler will be called when user change group
    """
    bot: Bot = query.bot
    user_id = query.from_user.id

    

    await bot.send_message(user_id, "Оберіть свою групу:", reply_markup=KB_CHOOSE_GROUP)


def register_users_handlers(dp: Dispatcher):

    # Message handlers
    
    dp.register_message_handler(__start, commands=["start", "restart"])

    # Callback handlers

    dp.register_callback_query_handler(__choose_group, text="continue_registration")

