import sqlite3
from aiogram import types
from create_bot import bot, Dispatcher


'''Connected database and made a cursor, made a list of all admin ids as well'''
def start_authorization():
    global base, cur, ids
    base = sqlite3.connect('bot_source/database/authorization.db')
    cur = base.cursor()
    cur.execute('SELECT ID FROM LogPass')
    ids = [row['id'] for row in cur]


async def authorization(msg):
    if msg.from_user.id in ids:
        cur.execute('SELECT Password FROM LogPass WHERE ID=?', msg.from_user.id)
        password = cur.fetchone()
        if password is None:
            print('good')

