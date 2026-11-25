from pydantic import BaseModel, Field


class EquationRequest(BaseModel):
    a: float = Field()
    b: float = Field()
    c: float = Field()