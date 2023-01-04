from typing import Final
import os

import aiomysql
import logging
from dotenv import load_dotenv # For local use only

load_dotenv() # For local use only



HOST = os.getenv('HOST')
PORT = int(os.getenv('DB_PORT'))
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
DB = os.getenv('DB')


async def open_connection():
    database = await aiomysql.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        db=DB
    )
    return database


async def select(sql):
    database = await open_connection()
    cursor = await database.cursor()
    await cursor.execute(sql)
    result = await cursor.fetchall()
    await cursor.close()
    database.close()
    return result


async def insert_update(sql, val):
    database = await open_connection()
    cursor = await database.cursor()
    await cursor.execute(sql, val)
    await database.commit()
    await cursor.close()
    database.close()
