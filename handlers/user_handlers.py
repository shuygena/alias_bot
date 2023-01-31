from copy import deepcopy
from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from database.database import Game, users_db 
from lexicon.lexicon import LEXICON
from keyboards.keyboards import get_new_game_keyboard

class FSMFillForm(StatesGroup):
    fill_teams_names = State()        # Состояние ожидания ввода названий команд

async def process_start_command(message: Message):
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = Game()   
    text = LEXICON[message.text]
    await message.answer(text = text, reply_markup = get_new_game_keyboard())

async def process_help_command(message: Message): 
    await message.answer(LEXICON[message.text])

async def process_rules_command(message: Message): 
    await message.answer(LEXICON[message.text])

async def process_game_command(message: Message): # todo
    await message.answer(LEXICON['/game'])
    await FSMFillForm.fill_teams_names.set()


async def process_game_press(callback: CallbackQuery):
    await callback.message.answer(LEXICON['/game'])
    await FSMFillForm.fill_teams_names.set()


async def process_teams_registration(message: Message, state: FSMContext):
    names_list = message.txt.split('\n')
    users_db[message.from_user.id].init_teams(names_list)
    await state.finish()
    # игра

async def warning_not_names(message: Message):
    await message.answer(text=LEXICON['not_names'])    

def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_start_command, commands=['game'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(process_rules_command, commands=['rules'])

    dp.register_callback_query_handler(process_game_press,
                                    text='new_game_button_pressed')

    dp.register_message_handler(process_teams_registration,
                                lambda x: len(x.text.split('\n')) > 0,
                                state=FSMFillForm.fill_teams_names)
    dp.register_message_handler(warning_not_names,
                            content_types='any',
                            state=FSMFillForm.fill_teams_names)
