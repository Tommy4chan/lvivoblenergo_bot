from bot.database.main import insert_update


async def create_user(user_id, user_info):
    await insert_update("INSERT INTO users (user_id, user_info) VALUES (%s, %s)", (str(user_id), str(user_info)))


