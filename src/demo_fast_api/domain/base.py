from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

dresseur_pokemon_association = Table(
    'dresseur_pokemon',
    Base.metadata,
    Column('dresseur_id', ForeignKey('dresseur.id')),
    Column('pokemon_id', ForeignKey('pokemon.id')),
)