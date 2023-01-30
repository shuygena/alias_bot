from dataclasses import dataclass
from environs import environs

@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str = None) -> Config:
    env = Env()
    try:
        env.read_env(path)
        return Config(tg_bot = TgBot(token = ))