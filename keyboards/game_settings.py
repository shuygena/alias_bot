from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_language_kb() -> InlineKeyboardMarkup:
    language_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    rus: InlineKeyboardButton = InlineKeyboardButton(text='Русский 🇷🇺',
                                                    callback_data='rus')
    eng: InlineKeyboardButton = InlineKeyboardButton(text='Английский 🇬🇧',
                                                    callback_data='eng')
    tau: InlineKeyboardButton = InlineKeyboardButton(text='Карачаево-балкарский 🏔',
                                                    callback_data='tau')
    language_kb.add(rus).add(eng).add(tau)
    return language_kb

def get_level_kb() -> InlineKeyboardMarkup:
    level_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    easy: InlineKeyboardButton = InlineKeyboardButton(text='🌕 Лёгкий',
                                                    callback_data='easy')
    norm: InlineKeyboardButton = InlineKeyboardButton(text='🌗 Нормальный',
                                                    callback_data='normal')
    hard: InlineKeyboardButton = InlineKeyboardButton(text='🌑 Сложный',
                                                    callback_data='hard')
    level_kb.add(easy).add(norm).add(hard)
    return level_kb

def get_pass_tax_kb() -> InlineKeyboardMarkup:
    pass_tax_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    yes: InlineKeyboardButton = InlineKeyboardButton(text='Отнимать 👎',
                                                    callback_data='True')
    no: InlineKeyboardButton = InlineKeyboardButton(text='Не отнимать 👍',
                                                    callback_data='False')
    pass_tax_kb.add(no, yes)
    return pass_tax_kb
