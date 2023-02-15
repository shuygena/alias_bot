from dataclasses import dataclass, field
from typing import Dict, List

RUS: str = 'rus'
ENG: str = 'eng'
EASY: str = 'easy'
NORMAL: str = 'normal'
HARD: str = 'hard'
TAU: str = 'tau'


@dataclass
class Game:
    is_in_game: bool = False
    language: str = RUS
    level: str = NORMAL
    time: int = 60
    score_to_win: int = 100
    pass_tax: bool = False
    time_is_over: bool = False
    current_team: int = 0
    current_word: int = 0
    previous_word: str = ''
    text: str = ''
    teams: Dict = field(default_factory=dict)
    game_words: List = field(default_factory=list)
    passed_words: List = field(default_factory=list)

    def reset_all(self):
        self.language = RUS
        self.level = NORMAL
        self.score_to_win = 100
        self.time = 60
        self.pass_tax = False

    def set_game_over(self):
        self.is_in_game = False
        self.time_is_over = False
        self.current_team: int = 0
        self.previous_word: str = ''
        self.text: str = ''
        self.teams = dict()
        self.game_words = list()
        self.passed_words = list()

    def set_previous_word(self, word: str):
        self.previous_word = word

    def get_previous_word(self) -> str:
        return self.previous_word

    def set_game_words(self, language: str, level: str):
        path = 'database/' + language + '_' + level + '.txt'
        self.game_words = load_list(path)

    def get_game_words(self) -> List:
        return self.game_words

    def remove_game_words(self, word: str):
        self.game_words.remove(word)

    def reset_game_words(self):
        language: str = self.language
        level: str = self.level
        path = 'database/' + language + '_' + level + '.txt'
        self.game_words = load_list(path)

    def set_text(self, text: str):
        self.text = text

    def get_text(self) -> str:
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

    def get_time(self) -> int:
        return self.time

    def set_time_is_over(self, is_over: bool):
        self.time_is_over = is_over

    def get_time_is_over(self) -> bool:
        return self.time_is_over

    def set_score_to_win(self, points: int):
        self.score_to_win = points

    def get_score_to_win(self) -> int:
        return self.score_to_win

    def set_pass_tax(self, tax: bool):
        self.pass_tax = tax

    def move_current_team(self):
        if (len(self.teams) == 1):
            self.current_team = 1
        else:
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

    def init_teams(self, teams_names: List):
        self.teams = ({i: {'name': team, 'score': 0} for i, team in enumerate(
                    teams_names, start=1) if len(team) > 0})

    def get_teams(self) -> Dict:
        return self.teams

    def calculate_score(self, team: int, guess: int = 0, pas: int = 0):
        self.teams[team]['score'] += (guess - self.pass_tax * pas)

    def get_info(self) -> str:
        if len(self.teams) == 0:
            return 'Нет зарегестрированных команд!'
        teams_info: List
        teams_info = [' '.join([str(i) + '.', self.teams[i]['name'] + ':',
                                str(self.teams[i]['score'])]) for i in range(
                                    1, 1 + len(self.teams))]
        info: str = '\n'.join(teams_info)
        return info


def load_list(path: str) -> Dict:
    with open(path, 'r') as f:
        lines = f.readlines()
    new_list = [line.strip('\n') for line in lines]
    return new_list


users_db: Dict = {}
