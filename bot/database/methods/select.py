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