from dataclasses import dataclass
from environs import Env
from typing import Dict

@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot = TgBot(token = env('BOT_TOKEN')))


def load_dict(path: str) -> Dict:
    with open(path, 'r') as f:
        lines = f.readlines()
    new_dict = {i: line.strip('\n') for i, line in enumerate(lines, start = 1)}
    return new_dict


def load_words() -> Dict:
    words = dict.fromkeys(['rus', 'eng'])
    words['rus'] = dict.fromkeys(['easy', 'normal', 'hard'])
    words['eng'] = dict.fromkeys(['easy', 'normal', 'hard'])
    words['rus']['easy'] = load_dict('config_data/rus_easy.txt')
    words['rus']['normal'] = load_dict('config_data/rus_normal.txt')
    words['rus']['hard'] = load_dict('config_data/rus_hard.txt')
    words['eng']['easy'] = load_dict('config_data/eng_easy.txt')
    words['eng']['normal'] = load_dict('config_data/eng_normal.txt')
    words['eng']['hard'] = load_dict('config_data/eng_hard.txt')
    return(words)
