import asyncio
import asyncpg
from dotenv import load_dotenv
import os


load_dotenv()

async def connect_to_db():
    conn = await asyncpg.connect(
        host=os.getenv('HOST'),
        database=os.getenv('DATABASE'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
    )
    return conn


async def create_table(conn):
    await conn.execute("""
        CREATE TABLE schedule_table (
            id serial PRIMARY KEY,
            faculty_name TEXT,
            course TEXT,
            group_name TEXT,
            week_number TEXT,
            discipline_name TEXT,
            plan_time_name TEXT,
            date TEXT,
            time TEXT,
            building_name TEXT,
            auditoriun_name TEXT,
            teacher_names TEXT
        );
    """)
    await conn.close()


async def main():
    conn = await connect_to_db()
    await create_table(conn)

asyncio.run(main())