import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from typing import Dict

from config_data.config import Config, load_config # i need it?
from database.database import words, users_db, RUS, ENG, EASY, NORMAL, HARD
from keyboards.main_menu import set_main_menu
from handlers.user_handlers import register_user_handlers
from handlers.game_handlers import register_game_handlers
from handlers.other_handlers import register_spam_handler

logger = logging.getLogger(__name__)


def register_all_handlers(dp: Dispatcher) -> None:
    register_user_handlers(dp)
    register_game_handlers(dp)
    register_spam_handler(dp)

async def main():
    logging.basicConfig(
        level = logging.INFO,
        format = u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting bot')
    storage: MemoryStorage = MemoryStorage()
    config: Config = load_config()
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode = 'HTML')
    dp: Dispatcher = Dispatcher(bot, storage = storage)
    await set_main_menu(dp)
    register_all_handlers(dp)
    try:
        await dp.start_polling()
    finally:
        await bot.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')