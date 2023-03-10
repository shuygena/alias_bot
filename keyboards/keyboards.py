from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_new_game_kb() -> InlineKeyboardMarkup:
    new_game_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    new_game_kb.add(InlineKeyboardButton(text='Начать игру',
                    callback_data='new_game_button_pressed'))
    return new_game_kb


def get_ready_kb() -> InlineKeyboardMarkup:
    ready_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    ready_kb.add(InlineKeyboardButton(
        text='Готовы!', callback_data='ready_button_pressed'))
    return ready_kb


def get_guess_pass_kb() -> InlineKeyboardMarkup:
    guess_pass_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    guess: InlineKeyboardButton
    pas: InlineKeyboardButton
    guess = InlineKeyboardButton(
        text='Угадали', callback_data='guess_button_pressed')
    pas = InlineKeyboardButton(
        text='Пропустить', callback_data='pass_button_pressed')
    guess_pass_kb.add(pas, guess)
    return guess_pass_kb
