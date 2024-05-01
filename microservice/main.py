import asyncpg
import aiohttp
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

async def get_faculties():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://lk.samgtu.ru/publics/api/cbfacultylist') as response:
            faculties = await response.json()
            return faculties

async def get_groups(faculty_id, course):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f'https://lk.samgtu.ru/publics/api/cbgrouplist?faculty_id={faculty_id}&course={course}') as response:
            groups = await response.json()
            return groups

async def get_schedule(group_id, week_number):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f'https://lk.samgtu.ru/publics/api/cbschedule?group_id={group_id}&week_number={week_number}') as response:
            schedule = await response.json()
            return schedule


async def insert_schedule(conn, dictionary, i):
    dictionary["BuildingName"] = dictionary["BuildingName"].replace('№', '')
    for key, value in dictionary.items():
        if value == "":
            dictionary[key] = "Не указано"

    query = (
        "INSERT INTO schedule_table (building_name, auditorium_name, plan_time_name, "
        "group_name, course, faculty_name, teacher_names, week_number, "
        "date, time, discipline_name) "
        "VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)"
    )

    await conn.execute(
        query,
        dictionary["BuildingName"], dictionary["AuditoriumName"],
        dictionary["PlanTimeTypeName"], dictionary["GroupName"], dictionary["Course"],
        dictionary["FacultyName"], dictionary["TeacherNames"], dictionary["WeekNumber"],
        dictionary["Date"], dictionary["Time"], dictionary["DisciplineName"]
    )


async def main():
    db_user = os.getenv('USER')
    db_password = os.getenv('PASSWORD')
    db_host = os.getenv('HOST')
    db_database = os.getenv('DATABASE')
    conn_pool = await asyncpg.create_pool(user=db_user, password=db_password, database=db_database, host=db_host)
    if conn_pool:
        print(db_database)
    i = 1


    faculties = await get_faculties()

    async with conn_pool.acquire() as conn:
        #for faculty in faculties.keys():
            for course in range(1, 7):
                groups = await get_groups(104717, course)
                for group in groups:
                    for week_number in range(1, 49):
                        schedule = await get_schedule(group['ID'], week_number)
                        if len(schedule) != 0:
                            for dictionary in schedule:
                                async with conn.transaction():
                                    await insert_schedule(conn, dictionary, i)
                                    i += 1

    await conn_pool.close()
    print('*********************************************Done**********************************************')


asyncio.run(main())
