from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from demo_fast_api.domain.base import Base


class Type(Base):
    __tablename__ = 'type'
    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(unique=True, nullable=False)
    couleur_hex: Mapped[str|None] = mapped_column(String(6))
    description: Mapped[str|None] = mapped_column()