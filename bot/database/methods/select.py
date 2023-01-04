from bot.database.main import select, open_connection

async def is_user_registered(user_id):
    return len(await select(f"SELECT * FROM users WHERE user_id = '{user_id}'"))


async def is_user_notfication_enabled(user_id):
    return len(await select(f"SELECT * FROM users WHERE user_id = '{user_id}' AND notification = '1'"))


async def get_user_group(user_id):
    return int((await select(f"SELECT user_group FROM users WHERE user_id = '{user_id}'"))[0][0])


async def get_all_users_with_enabled_notification():
    return await select("SELECT user_id FROM users WHERE notification = '1'")


async def get_all_users():
    return await select("SELECT user_id FROM users")


async def get_bot_notification_time():
    return (await select("SELECT notification_time FROM bot_settings"))[0][0]


async def is_user_admin(user_id):
    return len(await select(f"SELECT * FROM users WHERE user_id = '{user_id}' AND is_admin = '1'"))


async def is_failsafe_enabled():
    return int((await select("SELECT failsafe FROM bot_settings"))[0][0])