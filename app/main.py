from fastapi import FastAPI

from .config import load_config
from .spotify.router import spotify_router
from .system.router import system_router

config = load_config()


def create_application():
    application = FastAPI(
        title="MusicBox API",
        debug=True  # TODO: Remove debug mode
    )

    application.include_router(system_router)
    application.include_router(spotify_router)

    return application


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:create_application",
        factory=True,
        host=config.uvicorn.host,
        port=config.uvicorn.port,
        log_level=config.uvicorn.log_level,
        reload=config.uvicorn.reload,
    )
