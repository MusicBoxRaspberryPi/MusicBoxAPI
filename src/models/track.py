from dataclasses import dataclass


@dataclass
class Track:
    id: str

    def __post_init__(self):
        self.uri = f"spotify:track:{self.id}"
