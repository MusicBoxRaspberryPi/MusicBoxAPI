from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.container import Container
from app.spotify.exceptions import TrackNotFoundError, DeviceNotFoundError
from app.spotify.schemas import Device, CurrentDevice, Track
from app.spotify.service import SpotifyService

spotify_router = APIRouter()


@spotify_router.get("/device")
@inject
def get_current_device(
        reset: bool = False,
        spotify_service: SpotifyService = Depends(Provide[Container.spotify_service])
) -> CurrentDevice | dict:
    spotify_service.refresh_devices()

    if reset:
        spotify_service.reset_current_device_index()

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
    updated = spotify_service.refresh_devices()

    if not updated:
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
    updated = spotify_service.refresh_devices()

    if not updated:
        spotify_service.previous_device()

    current_device = spotify_service.get_current_device()

    if current_device is None:
        return {}

    return CurrentDevice(
        device=current_device,
        index=spotify_service.get_current_device_index(),
        total=spotify_service.get_devices_count()
    )


@spotify_router.post("/play")
@inject
def play(
        track: Track,
        spotify_service: SpotifyService = Depends(Provide[Container.spotify_service])
) -> Device | dict:
    try:
        spotify_service.play(track)
    except TrackNotFoundError:
        return {"error": "Track not found"}
    except DeviceNotFoundError:
        return {"error": "Device not found"}
    return {"status": "ok"}
