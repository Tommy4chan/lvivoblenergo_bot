from bot.database.main import Database
from bot.database.methods.other import is_user_registered

def register_user(user_id, user_info):
    database = Database()
    database.open_connection()
    cursor = database.DB.cursor()
    sql = "INSERT INTO users (user_id, user_info) VALUES (%s, %s)"
    val = (str(user_id), str(user_info))
    if is_user_registered(user_id):
        sql = f"UPDATE users SET user_info = %s WHERE user_id = %s"
        val = (str(user_info), str(user_id))
    cursor.execute(sql, val)
    database.DB.commit()
    database.close_connection()
