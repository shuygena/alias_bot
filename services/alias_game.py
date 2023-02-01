from random import randint, seed
from typing import Dict
from database.database import words

def generate_new_word(language: str, level: str) -> Dict:
    seed()
    number = randint(1, len(words[language][level]))
    return number, words[language][level][number]