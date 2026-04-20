from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer,String

class Doctor(Base):
    __tablename__ = 'doctors'

    id :Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String)
    specialization:Mapped[str] = mapped_column(String)
    max_daily_slots:Mapped[int] = mapped_column(Integer)