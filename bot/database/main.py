from typing import Final

import mysql.connector


class Database():
    DB: Final = None

    def __init__(self):
        self.DB = self.open_connection()

    def open_connection(self):
        return mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="",
            database="lvivoblenergo_bot_db",
            ssl_disabled = False
        )

    def close_connection(self):
        self.DB.close()
    
