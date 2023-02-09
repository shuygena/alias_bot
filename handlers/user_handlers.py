from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters import Text
from database.database import Game, users_db
from lexicon.lexicon import LEXICON
from keyboards.keyboards import get_new_game_kb, get_ready_kb, get_guess_pass_kb
from services.alias_game import generate_new_word
from keyboards.game_settings import get_language_kb, get_level_kb, get_pass_tax_kb

class FSMFillForm(StatesGroup):
    fill_teams_names = State()
    # set_language = State()
    # set_level = State()
    # set_pass_tax = State()


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


async def process_game_press(callback: CallbackQuery):
    await callback.message.answer(LEXICON['/game'])
    await FSMFillForm.fill_teams_names.set()


async def process_set_language_command(message: Message):
    await message.answer(LEXICON[message.text],
                        reply_markup = get_language_kb())
    

async def set_language(message: Message):
    user_id: int = message.from_user.id
    language: str = message.text.lower()
    users_db[user_id].set_language(language)


async def process_set_level_command(message: Message):
    await message.answer(LEXICON[message.text],
                        reply_markup = get_level_kb())

async def set_level(message: Message):
    user_id: int = message.from_user.id
    level: str = message.text.lower()
    users_db[user_id].set_level(level)

async def game_start(message: Message, state: FSMContext): # проверить на сброс параметров
    await state.finish()
    user_id: int = message.from_user.id
    names_list: List = message.text.split('\n')
    users_db[user_id].init_teams(names_list)
    users_db[user_id].set_game_status(True)
    users_db[user_id].move_current_team()
    users_db[user_id].reset_current_word()
    users_db[user_id].set_time_is_over(False)
    users_db[user_id].reset_game_words()
    team_name = users_db[user_id].get_teams()[1]['name']
    text = f'Очередь команды «{team_name}»\n\nГотовы?'
    
    await message.answer(text = text, reply_markup = get_ready_kb())


async def warning_not_names(message: Message):
    await message.answer(text=LEXICON['not_names'])


def register_user_handlers(dp: Dispatcher):
    dp.register_message_handler(process_start_command, commands=['start'])
    dp.register_message_handler(process_game_command, commands=['game'])
    dp.register_message_handler(process_help_command, commands=['help'])
    dp.register_message_handler(process_rules_command, commands=['rules'])
    dp.register_message_handler(process_info_command, commands=['info'])
    dp.register_message_handler(process_set_language_command,
                                commands=['set_language'])
    dp.register_message_handler(process_set_level_command,
                                commands=['set_level'])
    # dp.register_message_handler(process_set_score_to_win_command,
    #                             commands=['set_score_to_win'])
    # dp.register_message_handler(process_set_time_command,
    #                             commands=['set_time'])
    # dp.register_message_handler(process_set_pass_tax_command,
    #                             commands=['set_pass_tax'])
    # dp.register_message_handler(process_set_reset_command,
    #                             commands=['set_reset'])
    dp.register_message_handler(set_language,
                                Text(equals=['RUS', 'ENG', 'TAU']))
    dp.register_message_handler(set_level,
                                Text(equals=['EASY', 'NORMAL', 'HARD']))

    dp.register_callback_query_handler(process_game_press,
                                    text='new_game_button_pressed')

    dp.register_message_handler(game_start,
                                lambda x: len(x.text) > 0 and len(x.text.split('\n')) < 5,
                                state=FSMFillForm.fill_teams_names)

    dp.register_message_handler(warning_not_names,
                            content_types='any',
                            state=FSMFillForm.fill_teams_names)
