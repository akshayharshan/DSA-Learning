from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import Integer,String,Date,ForiegnKey

class Patient(Base):
    __tablename__ = "patients"


    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    age:Mapped[int] = mapped_column(String)

