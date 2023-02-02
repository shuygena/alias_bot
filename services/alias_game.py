from random import choice, seed
from typing import Set
from database.database import users_db

def generate_new_word(user_id) -> str:
    seed()
    game_words: Set = users_db[user_id].get_game_words()
    if len(game_words) == 0: # что если и len(passed_words) == 
        passed_words = users_db[user_id].get_passed_words()
        if len(passed_words) > 0:
            users_db[user_id].set_game_words(passed_words)
        else:
            users_db[user_id].reset_game_words()
        game_words = users_db[user_id].get_game_words()
        users_db[user_id].reset_passed_words()
    word: str = choice(game_words)
    users_db[user_id].remove_game_words(word)
    return word

def get_winner():
    pass