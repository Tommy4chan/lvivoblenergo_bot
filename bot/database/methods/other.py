from bot.database.main import Database

def is_user_registered(user_id):
    database = Database()
    database.open_connection()
    cursor = database.DB.cursor()
    sql = f"SELECT * FROM users WHERE user_id ='{user_id}'"
    cursor.execute(sql)
    res = cursor.fetchall()
    database.close_connection()
    return False if len(res) == 0 else True