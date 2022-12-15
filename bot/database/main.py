from typing import Final

import aiomysql


class Database():
    DB: Final = None

    async def open_connection(self):
        self.DB = await aiomysql.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="",
            db="lvivoblenergo_bot_db"
        )

    def close_connection(self):
        self.DB.close()
    
