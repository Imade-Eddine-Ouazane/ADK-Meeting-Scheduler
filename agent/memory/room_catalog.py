from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Room:
    city: str
    name: str
    capacity: int
    video: bool
    notes: str

ROOMS: List[Room] = [
    Room(city="Paris", name="Salle Rivoli", capacity=8, video=True, notes="Near Metro, whiteboard"),
    Room(city="Paris", name="Salle Louvre", capacity=16, video=True, notes="Projector, quiet"),
    Room(city="Lyon", name="Confluence 1", capacity=12, video=False, notes="Bright room"),
    Room(city="Lyon", name="Bellecour", capacity=20, video=True, notes="Large table"),
    Room(city="Marseille", name="Vieux-Port A", capacity=10, video=True, notes="Sea view"),
    Room(city="Marseille", name="Joliette B", capacity=6, video=False, notes="Budget option"),
]
