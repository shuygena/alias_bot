from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

words_card_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup()

def get_new_game_kb() -> InlineKeyboardMarkup:
    new_game_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    new_game_kb.add(InlineKeyboardButton(text = 'Начать игру',
                    callback_data='new_game_button_pressed'))
    return new_game_kb

def get_ready_kb() -> InlineKeyboardMarkup:
    ready_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    ready_kb.add(InlineKeyboardButton(text = 'Готовы!',
                    callback_data='ready_button_pressed'))
    return ready_kb

def get_guess_pass_kb() -> InlineKeyboardMarkup:
    guess_pass_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    guess_pass_kb.add(InlineKeyboardButton(text = 'Пропустить',
                    callback_data='pass_button_pressed'),
                    InlineKeyboardButton(text = 'Угадали',
                    callback_data='guess_button_pressed'))
    return guess_pass_kb


