class SpotifyError(Exception):
    """Base class for exceptions in this module."""
    pass


class TrackNotFoundError(SpotifyError):
    """Exception raised when a track is not found.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = message


class DeviceNotFoundError(SpotifyError):
    """Exception raised when a device is not found.

    Attributes:
        message -- explanation of the error
    """

    def __init__(self, message: str):
        self.message = message
