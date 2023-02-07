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
    time: int = 10
    score_to_win: int = 15 # не больше 250
    pass_tax : bool = False
    last_word_is_played: bool = False # if prolonged is possible
    time_is_over: bool = False
    current_team: int = 0 # номер текущей команды (чтобы отследить победителя)
    current_word: int = 0 # номер текущего слова, который будет отражаться в сообщении
    previous_word: str = ''
    text: str = ''
    teams: Dict = field(default_factory=dict)
    game_words: List = field(default_factory=list)
    passed_words: List = field(default_factory=list)# incapsulation ?
    
    def set_game_over (self):
        self.is_in_game = False
        self.time_is_over = False
        self.current_team: int = 0 
        previous_word: str = ''
        text: str = ''
        teams = dict()
        game_words = list()
        passed_words = list()

    def set_previous_word(self, word: str):
        self.previous_word = word

    def get_previous_word(self) -> str:
        return self.previous_word

    def set_game_words(self, language: str, level: str):
        self.game_words = words[language][level]

    def get_game_words(self) -> List:
        return self.game_words

    def remove_game_words(self, word: str):
        self.game_words.remove(word)

    def reset_game_words(self):
        self.game_words = words[self.language][self.level]

    def set_text(self, text: str):
        self.text = text

    def get_text(self) -> int:
        return self.text

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

    def get_time(self):
        return self.time

    def set_time_is_over(self, is_over: bool):
        self.time_is_over = bool
    
    def set_score_to_win(self, points: int):
        self.score_to_win = points

    def get_score_to_win(self) -> int:
        return self.score_to_win
    
    def set_pass_tax(self, tax: bool):
        self.pass_tax = bool
    
    def set_last_word_is_played(self, is_played: bool):
        self.last_word_is_played = is_played

    def get_last_word_is_played(self):
        return self.last_word_is_played

    def move_current_team(self):
        self.current_team = self.current_team % len(self.teams) + 1
    
    def get_current_team(self) -> int:
        return self.current_team

    def move_current_word(self):
        self.current_word += 1
    
    def get_current_word(self) -> int:
        return self.current_word

    def reset_current_word(self):
        self.current_word = 1
    
    def add_passed_word(self, word: str):
        self.passed_words.append(word)

    def get_passed_words(self) -> List:
        return self.passed_words

    def reset_passed_words(self):
        self.passed_words = list()
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



def load_list(path: str) -> Dict:
    with open(path, 'r') as f:
        lines = f.readlines()
    new_list = [line.strip('\n') for line in lines]
    return new_list


def load_words() -> Dict:
    words = dict.fromkeys([RUS, ENG])
    words[RUS] = dict.fromkeys([EASY, NORMAL, HARD])
    words[ENG] = dict.fromkeys([EASY, NORMAL, HARD])
    words[RUS][EASY] = load_list('database/rus_easy.txt')
    words[RUS][NORMAL] = load_list('database/rus_normal.txt')
    words[RUS][HARD] = load_list('database/rus_hard.txt')
    words[ENG][EASY] = load_list('database/eng_easy.txt')
    words[ENG][NORMAL] = load_list('database/eng_normal.txt')
    words[ENG][HARD] = load_list('database/eng_hard.txt')
    return(words)

words: Dict = load_words()
users_db: Dict = {}