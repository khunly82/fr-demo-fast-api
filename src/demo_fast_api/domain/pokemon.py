from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from demo_fast_api.domain.base import Base
from demo_fast_api.domain.nature import Nature

if TYPE_CHECKING:
    from demo_fast_api.domain.espece import Espece


class Pokemon(Base):
    __tablename__ = 'pokemon'
    id: Mapped[int] = mapped_column(primary_key=True)
    surnom: Mapped[str|None] = mapped_column()
    niveau: Mapped[int] = mapped_column(default=1)
    est_shiny: Mapped[bool] = mapped_column(default=False)
    nature: Mapped[Nature] = mapped_column(Enum(Nature), nullable=False)

    espece_numero_pokedex: Mapped[int] = mapped_column(ForeignKey('espece.numero_pokedex'))
    espece: Mapped[Espece] = relationship()