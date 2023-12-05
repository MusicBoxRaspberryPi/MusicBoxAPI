import spotipy

from src.exceptions import TrackNotFoundError, DeviceNotFoundError
from src.models import Track, Device


class Spotify:
    def __init__(
            self,
            client_id: str,
            client_secret: str,
            redirect_uri: str = "http://localhost:8080",
    ) -> None:
        self.__api = spotipy.Spotify(
            auth_manager=spotipy.SpotifyOAuth(
                client_id=client_id,
                client_secret=client_secret,
                redirect_uri=redirect_uri,
                scope="user-read-playback-state,user-modify-playback-state"
            )
        )

        self.__devices = self.__get_devices_from_api()
        self.__current_device_index = 0

    def play(self, track: Track) -> None:
        current_device = self.get_current_device()

        try:
            self.__api.transfer_playback(
                device_id=current_device.id,
                force_play=False
            )
            self.__api.start_playback(
                device_id=current_device.id,
                uris=[track.uri]
            )
        except spotipy.exceptions.SpotifyException as e:
            if "Device not found" in e.msg:
                raise DeviceNotFoundError(e.msg)
            elif "Invalid track uri" in e.msg:
                raise TrackNotFoundError(e.msg)

    def refresh_devices(self) -> list[Device]:
        self.__devices = self.__get_devices_from_api()
        self.__current_device_index = 0
        return self.__devices

    def next_device(self) -> Device | None:
        if len(self.__devices) == 0:
            return None

        self.__current_device_index = (self.__current_device_index + 1) % len(self.__devices)
        return self.get_current_device()

    def previous_device(self) -> Device | None:
        if len(self.__devices) == 0:
            return None

        self.__current_device_index = (self.__current_device_index - 1) % len(self.__devices)
        return self.get_current_device()

    def get_current_device(self) -> Device | None:
        if len(self.__devices) == 0:
            return None

        return self.__devices[self.__current_device_index]

    def get_devices(self) -> list[Device]:
        return self.__devices

    def __get_devices_from_api(self) -> list[Device]:
        devices_json = self.__api.devices()["devices"]
        return [Device(**device) for device in devices_json]


if __name__ == "__main__":
    from src.config import load_config

    config = load_config()

    sp = Spotify(
        client_id=config.spotify.client_id,
        client_secret=config.spotify.client_secret,
    )

    sp.play(Track(id="2bqS0QtnXGjOYs3z6VtSyW"))
