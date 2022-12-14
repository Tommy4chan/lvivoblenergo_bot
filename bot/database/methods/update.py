from bot.database.main import Database


def update_user(user_id, user_info):
    database = Database()
    cursor = database.DB.cursor()
    sql = f"UPDATE users SET user_info = %s WHERE user_id = %s"
    val = (str(user_info), str(user_id))
    cursor.execute(sql, val)
    database.DB.commit()
    database.close_connection()


def update_user_group(user_id, user_group):
    database = Database()
    cursor = database.DB.cursor()
    sql = f"UPDATE users SET user_group = %s WHERE user_id = %s"
    val = (str(user_group), str(user_id))
    cursor.execute(sql, val)
    database.DB.commit()
    database.close_connection()

def update_user_notification_state(user_id, notification):
    database = Database()
    cursor = database.DB.cursor()
    sql = f"UPDATE users SET notification = %s WHERE user_id = %s"
    val = (int(not notification), str(user_id))
    cursor.execute(sql, val)
    database.DB.commit()
    database.close_connection()