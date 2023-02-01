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
    score_to_win: int = 100 # не больше 500
    pass_tax : bool = False
    last_word_time: bool = False # if prolonged is possible
    current_team: int = 0
    current_word: int = 0
    # winner: Dict = field(default_factory=dict)
    teams: Dict = field(default_factory=dict)
    used_words: Set = field(default_factory=set)# incapsulation ?
    

    def set_game_status(self, is_in_game: bool):
        self.is_in_game = is_in_game

    def get_game_status(self) -> bool:
        return self.is_in_game
    
    def set_language(self, language: str):
        self.language = language
    
    def get_language(self) -> str:
        return self.language

    def set_level(self, level: str):
        self.level = level
    
    def get_level(self) -> str:
        return self.level
        
    def set_time(self, time: int):
        self.time = time
    
    def set_max_points(self, points: int):
        self.score_to_win = points
    
    def set_pass_tax(self, tax: bool):
        self.pass_tax = bool
    
    def set_last_word_time(self, prolonged: bool):
        self.last_word_time = prolonged

    def move_current_team(self):
        self.current_team = (self.current_team + 1) % len(self.teams)
    
    def get_current_team(self) -> int:
        return self.current_team

    def move_current_word(self):
        self.current_word += 1
    
    def get_current_word(self) -> int:
        return self.current_word
    
    def add_used_word(self, number: int):
        self.used_words.add(number)

    def get_used_words(self) -> Set:
        return self.used_words
    # def get_winner(self) -> Dict:
    #     return self.winner


    # def set_winner(self, name, score):
    #     self.winner['name'] = name
    #     self.winner['score'] = score
    
    def init_teams(self, teams_names: List): #убрать strip
        self.teams = {i: {'name': team, 'score': 0} for i, team in
        enumerate(teams_names, start = 1) if len(team) > 0}
    

    def get_teams(self) -> Dict:
        return self.teams

    def calculate_score(self, team: int, guess: int = 0, pas: int = 0):
        self.teams[team]['score'] += (guess - self.pass_tax * pas)
    
    def get_info(self):
        if len(self.teams) == 0:
            return 'Нет зарегестрированных команд!'
        teams_info_list: List = [' '.join([str(i) + '.',
                                self.teams[i]['name'] + ':',
                                str(self.teams[i]['score'])])
                                for i in range(1, 1 + len(self.teams))]
        info: str = '\n'.join(teams_info_list)
        return info



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