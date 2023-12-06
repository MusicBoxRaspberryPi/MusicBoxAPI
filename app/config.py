from dataclasses import dataclass

from environs import Env


@dataclass
class UvicornConfig:
    host: str
    port: int
    log_level: str
    reload: bool


@dataclass
class SpotifyConfig:
    client_id: str
    client_secret: str


@dataclass
class Config:
    uvicorn: UvicornConfig
    spotify: SpotifyConfig


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)

    return Config(
        uvicorn=UvicornConfig(
            host=env.str("UVICORN_HOST"),
            port=env.int("UVICORN_PORT"),
            log_level=env.str("UVICORN_LOG_LEVEL"),
            reload=env.bool("UVICORN_RELOAD")
        ),
        spotify=SpotifyConfig(
            client_id=env.str("SPOTIFY_CLIENT_ID"),
            client_secret=env.str("SPOTIFY_CLIENT_SECRET")
        )
    )
