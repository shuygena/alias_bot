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

def get_api_key(path = None) -> str:
    env = Env()
    env.read_env(path)
    return env('API_KEY')