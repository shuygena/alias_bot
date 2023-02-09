from random import choice, seed
from typing import Set, Dict
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


def control_len_text(text: str) -> str:
    lines = text.split('\n')
    lines.pop(4)
    text = ('\n').join(lines)
    return text

def find_max_score(teams: Dict, score_to_win):
    score_list = list()
    for key in teams:
        if (teams[key]['score'] >= score_to_win):
            score_list.append(teams[key]['score'])
    if len(score_list) == 0:
        return 0
    return max(score_list)  

def get_winner(user_id: int):
    teams = users_db[user_id].get_teams()
    winners = dict()
    max_score = find_max_score(teams, users_db[user_id].get_score_to_win())
    if max_score > 0:
        for key in teams:
            if (teams[key]['score'] == max_score):
                winners[key]= teams[key]
    return winners

# def generate_team_name():
#     names = """Шарлотка Бронте
# Пельмени Перельмана

# """
#     names_list = names.split('\n')
#     seed()
#     teams = list()
#     teams.append(choice())