from bot.database.main import Database
from bot.database.methods.insert import create_user
from bot.database.methods.update import update_user, update_failsafe_state
from bot.database.methods.select import is_user_registered, is_failsafe_enabled


async def register_user(user_id, user_info):
    if await is_user_registered(user_id):
        await update_user(user_id, user_info)
    else:
        await create_user(user_id, user_info)

async def change_failsafe_state():
    if await is_failsafe_enabled():
        await update_failsafe_state(0)
        return "Failsafe - вимкнено"
    else:
        await update_failsafe_state(1)
        return "Failsafe - увімкнено"