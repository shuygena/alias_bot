from requests import get, codes
from json import loads

from aiogram import Dispatcher
from aiogram.types import Message

from config_data.config import get_api_key

API_URL: str = 'https://api.api-ninjas.com/v1/loremipsum?paragraphs=1;random=true;max_length=50'
API_KEY: str = get_api_key()


async def send_spam(message: Message):
    response = get(API_URL, headers={'X-Api-Key': API_KEY})
    dict = loads(response.text)
    text: str = '<b>Я не понимаю, что ты пишешь.</b> 🧐\n'
    if response.status_code == codes.ok:
        text += 'Для меня это всё равно что:<i>\n' + dict['text'] + '</i>'
    await message.reply(text)


def register_spam_handler(dp: Dispatcher):
    dp.register_message_handler(send_spam)