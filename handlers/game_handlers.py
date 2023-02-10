from asyncio import sleep
from aiogram import Dispatcher
from aiogram.types import CallbackQuery, Message

from database.database import users_db
from lexicon.lexicon import LEXICON
from keyboards.keyboards import get_new_game_kb, get_ready_kb, get_guess_pass_kb
from services.alias_game import generate_new_word, control_len_text, get_winner


async def process_ready_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    word = generate_new_word(user_id)
    curr_word: int = users_db[user_id].get_current_word()
    text = callback.message.text + f'\n\n<b>{curr_word}. {word}</b>' 
    users_db[user_id].move_current_word()
    users_db[user_id].set_previous_word(word)
    users_db[user_id].set_time_is_over(False)
    await callback.message.edit_text(text=text,
                                    reply_markup=get_guess_pass_kb())
    users_db[user_id].set_text(text)
    await scheduler(callback, user_id)


async def process_guess_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    word = generate_new_word(user_id)
    curr_word: int = users_db[user_id].get_current_word()
    users_db[user_id].calculate_score(users_db[user_id].get_current_team(),
                                    guess = 1)
    if users_db[user_id].get_time_is_over() == True:
        await callback.message.edit_text(callback.message.text +
        ' ✅\n\n⌛️ <b>Время вышло!</b>')
        return None
    if curr_word <= 100:
        text = callback.message.text
    else:
        text = control_len_text(callback.message.text)
    text += f' ✅\n<b>{curr_word}. {word}</b>'
    users_db[user_id].move_current_word()
    users_db[user_id].set_previous_word(word)
    await callback.message.edit_text(text=text,
                                reply_markup=callback.message.reply_markup)
    users_db[user_id].set_text(text)
    

async def process_pass_press(callback: CallbackQuery):
    user_id = callback.from_user.id
    word = generate_new_word(user_id)
    curr_word: int = users_db[user_id].get_current_word()
    users_db[user_id].calculate_score(users_db[user_id].get_current_team(),
                                    pas = 1)
    if users_db[user_id].get_time_is_over() == True:
        await callback.message.edit_text(callback.message.text +
        ' ❌\n\n⌛️ <b>Время вышло!</b>')
        return None
    if curr_word <= 100:
        text = callback.message.text
    else:
        text = control_len_text(callback.message.text)
    text += f' ❌\n<b>{curr_word}. {word}</b>' 
    users_db[user_id].move_current_word()
    users_db[user_id].add_passed_word(users_db[user_id].get_previous_word())
    users_db[user_id].set_previous_word(word)
    await callback.message.edit_text(text=text,
                                reply_markup=callback.message.reply_markup)
    users_db[user_id].set_text(text)


async def round_start(message: Message, user_id: int):
    # winners = get_winner()
    # if winners == 1:
    #     await    
    users_db[user_id].move_current_team()
    users_db[user_id].reset_current_word()
    users_db[user_id].set_time_is_over(False)
    team_number = users_db[user_id].get_current_team()
    win = get_winner(user_id)
    if team_number == 1 and len(win) == 1:
        users_db[user_id].set_game_over()
        key = list(win.keys())[0]
        text = f"""🎉 Поздравляем!

Победила команда №{key} <b>{win[key]['name']}</b> со счётом {win[key]['score']}

Начать новую игру?"""
        await message.answer(text = text, reply_markup = get_new_game_kb())
    else:
        team_name = users_db[user_id].get_teams()[team_number]['name']
        text = f'Очередь команды «{team_name}»\n\nГотовы?'
        await message.answer(text = text, reply_markup = get_ready_kb())



async def scheduler (callback: CallbackQuery, id: int):
    await sleep(users_db[id].get_time())
    users_db[id].set_time_is_over(True)
    text = users_db[id].get_text()
    text = text.replace('<b>', '').replace('</b>','')
    text  += ' 🏁\n\n⌛️ <b>Время вышло!</b>'
    await callback.message.edit_text(text = text)
    if users_db[id].get_last_word_is_played() == False:
        # await sleep(1) # надеюсь, что не нужно, чтобы корректно отредактировать сообщение
        await round_start(callback.message, id)
    else:
        pass


def register_game_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(process_ready_press,
                                    text='ready_button_pressed')
    dp.register_callback_query_handler(process_guess_press,
                                    text='guess_button_pressed')
    dp.register_callback_query_handler(process_pass_press,
                                    text='pass_button_pressed')
