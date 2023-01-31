from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

words_card_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup()

def get_new_game_keyboard() -> InlineKeyboardMarkup:
    new_game_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    new_game_kb.add(InlineKeyboardButton(text = 'Начать игру',
                    callback_data='new_game_button_pressed'))
    return new_game_kb



