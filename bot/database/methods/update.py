from bot.database.main import insert_update


async def update_user(user_id, user_info):
    await insert_update("UPDATE users SET user_info = %s WHERE user_id = %s", (str(user_info), str(user_id)))


async def update_user_group(user_id, user_group):
    await insert_update("UPDATE users SET user_group = %s WHERE user_id = %s", (str(user_group), str(user_id)))


async def update_user_notification_state(user_id, notification):
    await insert_update("UPDATE users SET notification = %s WHERE user_id = %s", (int(not notification), str(user_id)))


async def update_failsafe_state(state):
    await insert_update("UPDATE bot_settings SET failsafe = %s", (state))