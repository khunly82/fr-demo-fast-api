from pydantic import BaseModel, Field


class EquationQuery(BaseModel):
    a: float = Field()
    b: float = Field()
    c: float = Field()