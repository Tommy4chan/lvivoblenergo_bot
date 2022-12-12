from bot.database.main import Database


def create_user(user_id, user_info):
    database = Database()
    database.open_connection()
    cursor = database.DB.cursor()
    sql = "INSERT INTO users (user_id, user_info) VALUES (%s, %s)"
    val = (str(user_id), str(user_info))
    cursor.execute(sql, val)
    database.DB.commit()
    database.close_connection()


