from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class CateringOption:
    city: str
    name: str
    per_person_eur: int
    diet: str
    notes: str

CATERING: List[CateringOption] = [
    CateringOption(city="Paris", name="Boulangerie Dupont", per_person_eur=12, diet="standard", notes="Sandwiches + boissons"),
    CateringOption(city="Paris", name="Veggie Box", per_person_eur=18, diet="vegetarian", notes="Assiettes veggie"),
    CateringOption(city="Lyon", name="Traiteur Rhône", per_person_eur=15, diet="standard", notes="Buffet froid"),
    CateringOption(city="Lyon", name="Sans Gluten+", per_person_eur=20, diet="gluten-free", notes="Option SG"),
    CateringOption(city="Marseille", name="Méditerranée", per_person_eur=16, diet="standard", notes="Tartes salées"),
    CateringOption(city="Marseille", name="Vegan Sud", per_person_eur=19, diet="vegan", notes="Menu vegan"),
]
