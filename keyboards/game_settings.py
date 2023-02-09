from aiogram.types import ReplyKeyboardMarkup, KeyboardButton # InlineKeyboardMarkup, InlineKeyboardButton

def get_language_kb() -> ReplyKeyboardMarkup:
    language_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                        resize_keyboard=True)
    rus: KeyboardButton = KeyboardButton('RUS')
    eng: KeyboardButton = KeyboardButton('ENG')
    tau: KeyboardButton = KeyboardButton('TAU')
    language_kb.add(rus, eng).add(tau)
    return language_kb

def get_level_kb() -> ReplyKeyboardMarkup:
    level_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                        resize_keyboard=True)
    easy: KeyboardButton = KeyboardButton('EASY')
    norm: KeyboardButton = KeyboardButton('NORMAL')
    hard: KeyboardButton = KeyboardButton('HARD')
    level_kb.add(easy).add(norm).add(hard)
    return level_kb

def get_pass_tax_kb() -> ReplyKeyboardMarkup:
    pass_tax_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(one_time_keyboard=True,
                                                        resize_keyboard=True)
    yes: KeyboardButton = KeyboardButton('Отнимать')
    no: KeyboardButton = KeyboardButton('Не отнимать')
    pass_tax_kb.add(no).add(yes)
    return pass_tax_kb
