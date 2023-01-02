from bot.database.main import Database

async def is_user_registered(user_id):
    database = Database()
    await database.open_connection()
    cursor = await database.DB.cursor()
    sql = f"SELECT * FROM users WHERE user_id = '{user_id}'"
    await cursor.execute(sql)
    result = await cursor.fetchall()
    database.close_connection()
    return len(result)


async def is_user_notfication_enabled(user_id):
    database = Database()
    await database.open_connection()
    cursor = await database.DB.cursor()
    sql = f"SELECT * FROM users WHERE user_id = '{user_id}' AND notification = '1'"
    await cursor.execute(sql)
    result = await cursor.fetchall()
    database.close_connection()
    return len(result)


async def get_user_group(user_id):
    database = Database()
    await database.open_connection()
    cursor = await database.DB.cursor()
    sql = f"SELECT user_group FROM users WHERE user_id = '{user_id}'"
    await cursor.execute(sql)
    result = await cursor.fetchone()
    database.close_connection()
    return int(result[0])


async def get_all_users_with_enabled_notification():
    database = Database()
    await database.open_connection()
    cursor = await database.DB.cursor()
    sql = f"SELECT user_id FROM users WHERE notification = '1'"
    await cursor.execute(sql)
    result = await cursor.fetchall()
    database.close_connection()
    return result


async def get_all_users():
    database = Database()
    await database.open_connection()
    cursor = await database.DB.cursor()
    sql = f"SELECT user_id FROM users"
    await cursor.execute(sql)
    result = await cursor.fetchall()
    database.close_connection()
    return result


async def get_bot_notification_time():
    database = Database()
    await database.open_connection()
    cursor = await database.DB.cursor()
    sql = f"SELECT notification_time FROM bot_settings"
    await cursor.execute(sql)
    result = await cursor.fetchone()
    database.close_connection()
    return result[0]


async def is_user_admin(user_id):
    database = Database()
    await database.open_connection()
    cursor = await database.DB.cursor()
    sql = f"SELECT * FROM users WHERE user_id = '{user_id}' AND is_admin = '1'"
    await cursor.execute(sql)
    result = await cursor.fetchall()
    database.close_connection()
    return len(result)


async def is_failsafe_enabled():
    database = Database()
    await database.open_connection()
    cursor = await database.DB.cursor()
    sql = f"SELECT failsafe FROM bot_settings"
    await cursor.execute(sql)
    result = await cursor.fetchone()
    database.close_connection()
    return int(result[0])