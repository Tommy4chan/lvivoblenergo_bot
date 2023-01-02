from typing import Final
import os

import aiomysql
from dotenv import load_dotenv # For local use only

load_dotenv() # For local use only


class Database():
    DB: Final = None

    async def open_connection(self):
        self.DB = await aiomysql.connect(
            host=os.getenv('HOST'),
            port=int(os.getenv('DB_PORT')),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            db=os.getenv('DB')
        )

    def close_connection(self):
        self.DB.close()
    
