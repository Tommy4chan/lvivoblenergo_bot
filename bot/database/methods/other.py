from bot.database.main import Database
from bot.database.methods.insert import create_user
from bot.database.methods.update import update_user
from bot.database.methods.select import is_user_registered


async def register_user(user_id, user_info):
    if await is_user_registered(user_id):
        await update_user(user_id, user_info)
    else:
        await create_user(user_id, user_info)