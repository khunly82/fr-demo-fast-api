from pydantic import BaseModel, Field


class EquationQuery(BaseModel):
    a: float = Field(lt=1000)
    b: float = Field()
    c: float = Field()