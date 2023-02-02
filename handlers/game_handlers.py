from asyncio import sleep
from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message

from database.database import users_db
from lexicon.lexicon import LEXICON
from keyboards.keyboards import get_new_game_kb, get_ready_kb, get_guess_pass_kb
from services.alias_game import generate_new_word


async def process_ready_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    word = generate_new_word(user_id)
    curr_word: int = users_db[user_id].get_current_word()
    text = callback.message.text + f'\n\n<b>{curr_word}. {word}</b>' 
    users_db[user_id].move_current_word()
    users_db[user_id].set_previous_word(word)
    await callback.message.edit_text(text=text,
                                    reply_markup=get_guess_pass_kb())
    users_db[user_id].set_text(text)
    await scheduler(callback, user_id)


async def process_guess_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    word = generate_new_word(user_id)
    curr_word: int = users_db[user_id].get_current_word()
    text = callback.message.text + f' ✅\n<b>{curr_word}. {word}</b>' 
    users_db[user_id].move_current_word()
    users_db[user_id].set_previous_word(word)
    users_db[user_id].calculate_score(users_db[user_id].get_current_team(),
                                    guess = 1)
    msg = await callback.message.edit_text(text=text,
                                reply_markup=callback.message.reply_markup)
    users_db[user_id].set_text(text)
    

async def process_pass_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    word = generate_new_word(user_id)
    curr_word: int = users_db[user_id].get_current_word()
    text = callback.message.text + f' ❌\n<b>{curr_word}. {word}</b>' 
    users_db[user_id].move_current_word()
    users_db[user_id].add_passed_word(users_db[user_id].get_previous_word())
    users_db[user_id].set_previous_word(word)
    users_db[user_id].calculate_score(users_db[user_id].get_current_team(),
                                    pas = 1)
    await callback.message.edit_text(text=text,
                                reply_markup=callback.message.reply_markup)
    users_db[user_id].set_text(text)


async def scheduler (callback: CallbackQuery, id: int):
    await sleep(users_db[id].get_time())
    text = users_db[id].get_text()
    text = text.replace('<b>', '').replace('</b>','')
    text  += ' 🏁\n\n⌛️ <b>Время вышло!</b>'
    await callback.message.edit_text(text = text)
    if users_db[id].get_last_word_is_played() == False:
        await round_start(callback.message, id)
    else:
        pass


async def round_start(message: Message, user_id: int):    
    users_db[user_id].move_current_team()
    users_db[user_id].reset_current_word()
    users_db[user_id].set_time_is_over(False)
    team_number = users_db[user_id].get_current_team()
    team_name = users_db[user_id].get_teams()[team_number]['name']
    text = f'Очередь команды «{team_name}»\n\nГотовы?'
    
    await message.answer(text = text, reply_markup = get_ready_kb())


def register_game_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(process_ready_press,
                                    text='ready_button_pressed')
    dp.register_callback_query_handler(process_guess_press,
                                    text='guess_button_pressed')
    dp.register_callback_query_handler(process_pass_press,
                                    text='pass_button_pressed')
