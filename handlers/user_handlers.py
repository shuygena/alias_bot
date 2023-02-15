from typing import List
from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from database.database import Game, users_db
from lexicon.lexicon import LEXICON
from keyboards.keyboards import get_new_game_kb, get_ready_kb
from keyboards.game_settings import (
        get_language_kb, get_level_kb, get_pass_tax_kb)


class FSMFillForm(StatesGroup):
    # in_game = State()
    set_teams_names = State()
    set_language = State()
    set_level = State()
    set_pass_tax = State()
    set_time = State()
    set_score_to_win = State()


async def process_start_command(message: Message):
    if message.from_user.id not in users_db:
        users_db[message.from_user.id] = Game()
    text = LEXICON[message.text]
    await message.answer(text=text, reply_markup=get_new_game_kb())


async def process_help_command(message: Message):
    await message.answer(LEXICON[message.text])


async def process_rules_command(message: Message):
    await message.answer(LEXICON[message.text])


async def process_info_command(message: Message):
    await message.answer(users_db[message.from_user.id].get_info())


async def process_game_command(message: Message):
    await message.answer(LEXICON[message.text])
    await FSMFillForm.set_teams_names.set()


async def process_game_press(callback: CallbackQuery):
    await callback.message.answer(LEXICON['/game'])
    await FSMFillForm.set_teams_names.set()


async def warning_not_names(message: Message):
    await message.answer(text=LEXICON['not_names'])


async def game_start(message: Message, state: FSMContext):
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
    await message.answer(text=text, reply_markup=get_ready_kb())


async def process_set_language_command(message: Message):
    await message.answer(LEXICON[message.text], reply_markup=get_language_kb())
    await FSMFillForm.set_language.set()


async def set_language(callback: CallbackQuery, state: FSMContext):
    await state.finish()
    user_id: int = callback.from_user.id
    language: str = callback.data
    users_db[user_id].set_language(language)
    await callback.answer()
    await callback.message.edit_text(
        text=LEXICON['/set_language'] +
        '\n\n⚙️ <b>Настройки сохранены!</b> /game')


async def warning_not_language(message: Message):
    await message.answer(LEXICON['use_buttons'])


async def process_set_level_command(message: Message):
    await message.answer(LEXICON[message.text], reply_markup=get_level_kb())
    await FSMFillForm.set_level.set()


async def set_level(callback: CallbackQuery, state: FSMContext):
    await state.finish()
    user_id: int = callback.from_user.id
    level: str = callback.data
    users_db[user_id].set_level(level)
    await callback.answer()
    await callback.message.edit_text(
        text=callback.message.text +
        '\n\n⚙️ <b>Настройки сохранены!</b> /game')


async def warning_not_level(message: Message):
    await message.answer(LEXICON['use_buttons'])


async def process_set_pass_tax_command(message: Message):
    await message.answer(LEXICON[message.text], reply_markup=get_pass_tax_kb())
    await FSMFillForm.set_pass_tax.set()


async def set_pass_tax(callback: CallbackQuery, state: FSMContext):
    await state.finish()
    user_id: int = callback.from_user.id
    pass_tax: str = callback.data
    if pass_tax == 'True':
        users_db[user_id].set_pass_tax(True)
    else:
        users_db[user_id].set_pass_tax(False)
    await callback.answer()
    await callback.message.edit_text(
        text=callback.message.text +
        '\n\n⚙️ <b>Настройки сохранены!</b> /game')


async def warning_not_tax(message: Message):
    await message.answer(LEXICON['use_buttons'])


async def process_set_time_command(message: Message):
    await message.answer(LEXICON[message.text])
    await FSMFillForm.set_time.set()


async def set_time(message: Message, state: FSMContext):
    await state.finish()
    user_id: int = message.from_user.id
    time: str = int(message.text)
    users_db[user_id].set_time(time)
    await message.answer('⚙️ <b>Настройки сохранены!</b> /game')


async def warning_not_time(message: Message):
    await message.answer(text='Введи число от 10 до 300 ❗️')


async def process_set_score_to_win_command(message: Message):
    await message.answer(LEXICON[message.text])
    await FSMFillForm.set_score_to_win.set()


async def set_score_to_win(message: Message, state: FSMContext):
    await state.finish()
    user_id: int = message.from_user.id
    score_to_win: str = int(message.text)
    users_db[user_id].set_score_to_win(score_to_win)
    await message.answer('⚙️ <b>Настройки сохранены!</b> /game')


async def warning_not_score_to_win(message: Message):
    await message.answer(text='Введи число от 1 до 200 ❗️')


async def process_set_reset_command(message: Message):
    await message.answer('⚙️ <b>Настройки сброшены!</b> /game')
    user_id: int = message.from_user.id
    users_db[user_id].reset_all()


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
    dp.register_message_handler(process_set_pass_tax_command,
                                commands=['set_pass_tax'])
    dp.register_message_handler(process_set_score_to_win_command,
                                commands=['set_score_to_win'])
    dp.register_message_handler(process_set_time_command,
                                commands=['set_time'])
    dp.register_message_handler(process_set_reset_command,
                                commands=['reset'])

    dp.register_callback_query_handler(
        set_language, text=['rus', 'eng', 'tau'],
        state=FSMFillForm.set_language)
    dp.register_callback_query_handler(
        set_level, text=['easy', 'normal', 'hard'],
        state=FSMFillForm.set_level)
    dp.register_callback_query_handler(
        set_pass_tax, text=['True', 'False'],
        state=FSMFillForm.set_pass_tax)
    dp.register_callback_query_handler(
        process_game_press, text='new_game_button_pressed')

    dp.register_message_handler(
        game_start, lambda x: len(x.text) > 0 and len(x.text.split('\n')) < 5,
        state=FSMFillForm.set_teams_names)
    dp.register_message_handler(
        set_time, lambda x: x.text.isdigit() and 10 <= int(x.text) <= 300,
        state=FSMFillForm.set_time)
    dp.register_message_handler(
        set_score_to_win,
        lambda x: x.text.isdigit() and 1 <= int(x.text) <= 200,
        state=FSMFillForm.set_score_to_win)

    dp.register_message_handler(
        warning_not_names, content_types='any',
        state=FSMFillForm.set_teams_names)
    dp.register_message_handler(
        warning_not_language, content_types='any',
        state=FSMFillForm.set_language)
    dp.register_message_handler(
        warning_not_level, content_types='any',
        state=FSMFillForm.set_level)
    dp.register_message_handler(
        warning_not_tax, content_types='any',
        state=FSMFillForm.set_pass_tax)
    dp.register_message_handler(
        warning_not_time, content_types='any',
        state=FSMFillForm.set_time)
    dp.register_message_handler(
        warning_not_score_to_win, content_types='any',
        state=FSMFillForm.set_score_to_win)
