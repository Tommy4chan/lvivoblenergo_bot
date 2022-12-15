from bot.database.main import Database


async def create_user(user_id, user_info):
    database = Database()
    await database.open_connection()
    cursor = await database.DB.cursor()
    sql = "INSERT INTO users (user_id, user_info) VALUES (%s, %s)"
    val = (str(user_id), str(user_info))
    await cursor.execute(sql, val)
    await database.DB.commit()
    database.close_connection()


