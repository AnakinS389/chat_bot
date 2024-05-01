'''
   Start Bot
'''

from aiogram import executor
from create_bot import dp
from bot_source.handlers import client
from bot_source.database import database_schedule
import logging


async def on_startup(_):
    await set_logging()
    logger.info('Bot has started to work')
    print('Bot is online')
    database_schedule.start_sqlite()


#  set up logging
async def set_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

logger = logging.getLogger('SamGTUbot')

#  registration handlers for client
client.register_handlers_client(dp)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)




