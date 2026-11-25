from pydantic import BaseModel, Field, EmailStr, PositiveFloat, NegativeFloat


class EquationRequest(BaseModel):
    a: PositiveFloat|NegativeFloat = Field()
    b: float = Field()
    c: float = Field()

class ContactRequest(BaseModel):
    name: str = Field(max_length=50)
    email: EmailStr = Field()
    content: str = Field(max_length=1000)