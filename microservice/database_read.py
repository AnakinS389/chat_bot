import asyncpg
import aiohttp
import asyncio
from dotenv import load_dotenv
пшimport os

load_dotenv()


async def read_from_db(conn, state):
    async with state.proxy() as data:
        sql = "SELECT * FROM schedule_table WHERE faculty_name=$1 AND course=$2 AND group_name=$3 AND date=$4"
        result = await conn.fetch(sql, data['faculty_name'], data['course'], data['group_name'], data['date'])
        return result


async def main(state):
    db_user = 'db_admin'
    db_password = 'db_admin'
    db_host = 'localhost'
    db_database = 'postgres'
    conn_pool = await asyncpg.create_pool(user=db_user, password=db_password, database=db_database, host=db_host)

    async with conn_pool.acquire() as conn:
        async with conn.transaction():
            result = await read_from_db(conn, state)
    await conn_pool.close()
    return result
