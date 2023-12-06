from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import TypeAdapter

from app.container import Container
from app.spotify.router import spotify_router
from app.system.router import system_router

load_dotenv()
container = Container()


def create_application() -> FastAPI:
    application = FastAPI(
        title="MusicBox API",
        debug=True
    )

    application.include_router(system_router)
    application.include_router(spotify_router)

    return application


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:create_application",
        factory=True,
        host=container.config.uvicorn.host(),
        port=int(container.config.uvicorn.port()),
        log_level=container.config.uvicorn.log_level(),
        reload=TypeAdapter(bool).validate_python(container.config.uvicorn.reload()),
    )
