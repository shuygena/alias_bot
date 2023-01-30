from dataclasses import dataclass
from environs import environs

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
