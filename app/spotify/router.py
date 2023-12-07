from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.container import Container
from app.spotify.schemas import Device, CurrentDevice
from app.spotify.service import SpotifyService

spotify_router = APIRouter()


@spotify_router.get("/device")
@inject
def get_current_device(
        spotify_service: SpotifyService = Depends(Provide[Container.spotify_service])
) -> CurrentDevice | dict:
    spotify_service.refresh_devices()
    current_device = spotify_service.get_current_device()

    if current_device is None:
        return {}

    return CurrentDevice(
        device=current_device,
        index=spotify_service.get_current_device_index(),
        total=spotify_service.get_devices_count()
    )


@spotify_router.post("/device/next")
@inject
def next_device(
        spotify_service: SpotifyService = Depends(Provide[Container.spotify_service])
) -> CurrentDevice | dict:
    spotify_service.refresh_devices()
    spotify_service.next_device()
    current_device = spotify_service.get_current_device()

    if current_device is None:
        return {}

    return CurrentDevice(
        device=current_device,
        index=spotify_service.get_current_device_index(),
        total=spotify_service.get_devices_count()
    )


@spotify_router.post("/device/previous")
@inject
def previous_device(
        spotify_service: SpotifyService = Depends(Provide[Container.spotify_service])
) -> CurrentDevice | dict:
    spotify_service.refresh_devices()
    spotify_service.previous_device()
    current_device = spotify_service.get_current_device()

    if current_device is None:
        return {}

    return CurrentDevice(
        device=current_device,
        index=spotify_service.get_current_device_index(),
        total=spotify_service.get_devices_count()
    )
