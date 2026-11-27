from dataclasses import dataclass, field

from pydantic import BaseModel

from demo_fast_api.domain.type import Type


@dataclass
class EquationResponse:
    delta: float
    sol1: float|None = field(default=None)
    sol2: float|None = field(default=None)

class TypeResponse(BaseModel):
    id: int
    nom: str
    couleur_hex: str

class TypeDetailsResponse(TypeResponse):
    description: str
    nb_especes: int