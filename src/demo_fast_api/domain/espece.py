from __future__ import annotations

from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import DECIMAL, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from demo_fast_api.domain.base import Base

if TYPE_CHECKING:
    from demo_fast_api.domain.type import Type


class Espece(Base):
    __tablename__ = 'espece'
    numero_pokedex: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=False
    )
    nom: Mapped[str] = mapped_column(unique=True, nullable=False)
    taille_m: Mapped[Decimal] = mapped_column(DECIMAL(7, 1), nullable=False)
    poids_kg: Mapped[Decimal] = mapped_column(DECIMAL(7, 1), nullable=False)
    description: Mapped[str|None] = mapped_column(nullable=True)

    type1_id: Mapped[int] = mapped_column(ForeignKey('type.id'), nullable=False)
    type2_id: Mapped[int|None] = mapped_column(ForeignKey('type.id'), nullable=True)

    type1: Mapped[Type] = relationship(foreign_keys=[type1_id])
    type2: Mapped[Type|None] = relationship(foreign_keys=[type2_id])