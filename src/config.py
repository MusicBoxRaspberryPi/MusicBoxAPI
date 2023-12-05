from dataclasses import dataclass

from environs import Env


@dataclass
class SpotifyConfig:
    client_id: str
    client_secret: str


@dataclass
class Config:
    spotify: SpotifyConfig


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        spotify=SpotifyConfig(
            client_id=env.str("SPOTIFY_CLIENT_ID"),
            client_secret=env.str("SPOTIFY_CLIENT_SECRET")
        )
    )
