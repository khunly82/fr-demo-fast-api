from pydantic import BaseModel, Field, EmailStr, PositiveFloat, NegativeFloat, field_validator


class EquationRequest(BaseModel):
    a: PositiveFloat|NegativeFloat = Field()
    b: float = Field()
    c: float = Field()

class ContactRequest(BaseModel):
    name: str = Field(max_length=50)
    email: EmailStr = Field()
    content: str = Field(max_length=1000)

class TypeRequest(BaseModel):
    nom: str = Field(max_length=100)
    couleur_hex: str = Field(pattern=r'^[A-F0-9]{6}$')
    description: str = Field(max_length=1000)

    @field_validator('nom')
    @classmethod
    def format_nom(cls, value: str):
        return value.title()