from sqlalchemy.orm import mapped_column,Mapped
from sqlalchemy import Integer,String,Date,ForiegnKey

class Appointment(Base):
    __tablename__ = 'appointments'

id : Mapped[int] = mapped_column(primary_key=True)
patient_id:Mapped[int] = mappped_column(ForiegnKey('patients.id'))
doctor_id:Mapped[int] = mapped_column(ForiegnKey('doctors.id'))
appointment_date : Mapped[Date]

