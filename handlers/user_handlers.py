from copy import deepcopy
from datetime import datetime, timedelta
from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from database.database import Game, users_db
from lexicon.lexicon import LEXICON
from keyboards.keyboards import get_new_game_kb, get_ready_kb, get_guess_pass_kb
from services.alias_game import generate_new_word

class FSMFillForm(StatesGroup):
    fill_teams_names = State()


async def process_start_command(message: Message):
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = Game()   
    text = LEXICON[message.text]
    await message.answer(text = text, reply_markup = get_new_game_kb())


async def process_help_command(message: Message): 
    await message.answer(LEXICON[message.text])


async def process_rules_command(message: Message): 
    await message.answer(LEXICON[message.text])

async def process_info_command(message: Message): 
    await message.answer(users_db[message.from_user.id].get_info())


async def process_game_command(message: Message):
    await message.answer(LEXICON[message.text])
    await FSMFillForm.fill_teams_names.set()

async def game_process(message: Message, state: FSMContext):
    await state.finish()
    user_id: int = message.from_user.id
    names_list: List = message.text.split('\n')
    users_db[user_id].init_teams(names_list)
    users_db[user_id].set_game_status(True)
    users_db[user_id].move_current_team()
    users_db[user_id].move_current_word()
    team_name = users_db[user_id].get_teams()[1]['name']
    text = f'Очередь команды «{team_name}»\n\nГотовы?'
    
    await message.answer(text = text, reply_markup = get_ready_kb())


async def process_game_press(callback: CallbackQuery):
    await callback.message.answer(LEXICON['/game'])
    await FSMFillForm.fill_teams_names.set()

async def process_ready_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    word = generate_new_word(users_db[user_id].get_language(),
                            users_db[user_id].get_level())
    while word[0] in users_db[user_id].get_used_words():
        word = generate_new_word(users_db[user_id].get_language(),
                                users_db[user_id].get_level())
    curr_word: int = users_db[user_id].get_current_word()
    text = callback.message.text + f'\n\n<b>{curr_word}. {word[1]}</b>' 
    users_db[user_id].add_used_word(word[0])
    users_db[user_id].move_current_word()
    await callback.message.edit_text(text=text,
                                    reply_markup=get_guess_pass_kb())


async def process_guess_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    word = generate_new_word(users_db[user_id].get_language(),
                            users_db[user_id].get_level())
    while word[0] in users_db[user_id].get_used_words():
        word = generate_new_word(users_db[user_id].get_language(),
                                users_db[user_id].get_level())
    curr_word: int = users_db[user_id].get_current_word()
    text = callback.message.text + f' ✅\n<b>{curr_word}. {word[1]}</b>' 
    users_db[user_id].add_used_word(word[0])
    users_db[user_id].move_current_word()
    users_db[user_id].calculate_score(users_db[user_id].get_current_team(),
                                    guess = 1)
    await callback.message.edit_text(text=text,
                                reply_markup=callback.message.reply_markup)
    

async def process_pass_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    word = generate_new_word(users_db[user_id].get_language(),
                            users_db[user_id].get_level())
    while word[0] in users_db[user_id].get_used_words():
        word = generate_new_word(users_db[user_id].get_language(),
                                users_db[user_id].get_level())
    curr_word: int = users_db[user_id].get_current_word()
    text = callback.message.text + f' ❌\n<b>{curr_word}. {word[1]}</b>' 
    users_db[user_id].add_used_word(word[0])
    users_db[user_id].move_current_word()
    users_db[user_id].calculate_score(users_db[user_id].get_current_team(),
                                    pas = 1)
    await callback.message.edit_text(text=text,
                                reply_markup=callback.message.reply_markup)


async def warning_not_names(message: Message):
    await message.answer(text=LEXICON['not_names'])    


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_game_command, commands=['game'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(process_rules_command, commands=['rules'])
    dp.register_message_handler(process_info_command, commands=['info'])

    dp.register_callback_query_handler(process_game_press,
                                    text='new_game_button_pressed')
    dp.register_callback_query_handler(process_ready_press,
                                    text='ready_button_pressed')
    dp.register_callback_query_handler(process_guess_press,
                                    text='guess_button_pressed')
    dp.register_callback_query_handler(process_pass_press,
                                    text='pass_button_pressed')

    dp.register_message_handler(game_process,
                                lambda x: len(x.text) > 0 and len(x.text.split('\n')) < 21,
                                state=FSMFillForm.fill_teams_names)
    dp.register_message_handler(warning_not_names,
                            content_types='any',
                            state=FSMFillForm.fill_teams_names)
