from bot.database.main import Database

def is_user_registered(user_id):
    database = Database()
    database.open_connection()
    cursor = database.DB.cursor()
    sql = f"SELECT * FROM users WHERE user_id = '{user_id}'"
    cursor.execute(sql)
    result = cursor.fetchall()
    database.close_connection()
    return len(result)


def is_user_notfication_enabled(user_id):
    database = Database()
    database.open_connection()
    cursor = database.DB.cursor()
    sql = f"SELECT * FROM users WHERE user_id = '{user_id}' AND notification = '1'"
    cursor.execute(sql)
    result = cursor.fetchall()
    database.close_connection()
    return len(result)


def get_user_group(user_id):
    database = Database()
    database.open_connection()
    cursor = database.DB.cursor()
    sql = f"SELECT user_group FROM users WHERE user_id = '{user_id}'"
    cursor.execute(sql)
    result = cursor.fetchone()[0]
    database.close_connection()
    return int(result)