import asyncio
import logging

from aiogram import Bot, Dispatcher
from typing import Dict

from config_data.config import Config, load_config, load_words

async def main():
    config: Config = load_config()
    words: Dict = load_words()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('Bot stopped!')