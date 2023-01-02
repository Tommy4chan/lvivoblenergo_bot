from aiogram import Dispatcher

from bot.handlers.user import register_users_handlers
from bot.handlers.admin import register_admin_handlers


def register_all_handlers(dp: Dispatcher):
    register_users_handlers(dp)
    register_admin_handlers(dp)