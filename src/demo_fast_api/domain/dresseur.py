from sqlalchemy.orm import Mapped, mapped_column

from demo_fast_api.domain.base import Base


class Dresseur(Base):
    __tablename__ = 'dresseur'
    id: Mapped[int] = mapped_column(primary_key=True)
    pseudo: Mapped[str] = mapped_column(nullable=False)
    ville: Mapped[str|None] = mapped_column()
    badges: Mapped[int] = mapped_column(default=0)
    actif: Mapped[bool] = mapped_column(default=True)