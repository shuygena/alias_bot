from dataclasses import dataclass, field
from environs import Env
from typing import Dict, Set, List

RUS = 'rus'
ENG = 'eng'
EASY = 'easy'
NORMAL = 'normal'
HARD = 'hard'

@dataclass
class Game:
    is_in_game: bool = False
    language: str = RUS
    level: str = NORMAL
    time: int = 90
    max_points: int = 100 # не больше 1000
    pass_tax : bool = False
    last_word_time: bool = False # if prolonged is possible
    teams: Dict = field(default_factory=dict)
    used_words: Set = field(default_factory=set)# incapsulation ?
    

    def set_game_status(is_in_game: bool):
        self.is_in_game = is_in_game
    
    def set_language(language: str):
        self.language = language
    
    def set_level(level: str):
        self.level = level
    
    def set_time(time: int):
        self.time = time
    
    def set_max_points(points: int):
        self.points = points
    
    def set_pass_tax(tax: bool):
        self.pass_tax = bool
    
    def set_last_word_time(prolonged: bool):
        self.last_word_time = prolonged
    
    def init_teams(teams_names: List): #убрать strip
        self.teams = {i: {'name': team.strip('\n'), 'points': 0} for i, team in
        enumerate(teams, start = 1)}

    def calculate_points(team, guessed, passed):
        self.teams[team] += guessed - self.pass_tax * passed
    
    def get_info():
        pass


def load_dict(path: str) -> Dict:
    with open(path, 'r') as f:
        lines = f.readlines()
    new_dict = {i: line.strip('\n') for i, line in enumerate(lines, start = 1)}
    return new_dict


def load_words() -> Dict:
    words = dict.fromkeys([RUS, ENG])
    words[RUS] = dict.fromkeys([EASY, NORMAL, HARD])
    words[ENG] = dict.fromkeys([EASY, NORMAL, HARD])
    words[RUS][EASY] = load_dict('database/rus_easy.txt')
    words[RUS][NORMAL] = load_dict('database/rus_normal.txt')
    words[RUS][HARD] = load_dict('database/rus_hard.txt')
    words[ENG][EASY] = load_dict('database/eng_easy.txt')
    words[ENG][NORMAL] = load_dict('database/eng_normal.txt')
    words[ENG][HARD] = load_dict('database/eng_hard.txt')
    return(words)

words: Dict = load_words()
users_db: Dict = {}