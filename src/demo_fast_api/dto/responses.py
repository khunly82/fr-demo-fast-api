from dataclasses import dataclass, field


@dataclass
class EquationResponse:
    delta: float
    sol1: float|None = field(default=None)
    sol2: float|None = field(default=None)