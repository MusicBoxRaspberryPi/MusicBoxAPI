from dataclasses import dataclass

@dataclass
class Device:
    id: str
    is_active: bool
    is_private_session: bool
    is_restricted: bool
    name: str
    supports_volume: bool
    type: str
    volume_percent: int
