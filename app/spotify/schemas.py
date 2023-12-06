from pydantic import BaseModel


class Device(BaseModel):
    id: str
    is_active: bool
    is_private_session: bool
    is_restricted: bool
    name: str
    supports_volume: bool
    type: str
    volume_percent: int


class Track(BaseModel):
    id: str

    @property
    def uri(self):
        return f"spotify:track:{self.id}"
