from fastapi import APIRouter
from fastapi_restful.cbv import cbv

from .service import SpotifyService

spotify_router = APIRouter()


@cbv(spotify_router)
class SpotifyController:
    def __init__(self):
        self.spotify_service = SpotifyService()

    @spotify_router.get("/devices")
    def get_devices(self):
        return self.spotify_service.get_devices()
