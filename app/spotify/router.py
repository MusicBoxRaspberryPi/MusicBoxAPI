from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.container import Container
from app.spotify.schemas import Device
from app.spotify.service import SpotifyService

spotify_router = APIRouter()


@spotify_router.get("/devices")
@inject
def get_devices(
        spotify_service: SpotifyService = Depends(Provide[Container.spotify_service]),
) -> list[Device]:
    return spotify_service.refresh_devices()
