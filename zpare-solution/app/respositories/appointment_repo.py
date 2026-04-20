from sqlalchemy import select, func
from models.appointment import Appointment
from sqlalchemy.orm import Session
from app.core.database import get_db
from FastAPI import Depends

class AppointmentRepository:

    def count_by_doctor_date(self, db: Session = Depends(get_db), doctor_id: int, date):
        stmt = select(func.count()).where(
            Appointment.doctor_id == doctor_id,
            Appointment.appointment_date == date
        )

        return db.execute(stmt).scalar()
    def create(self, db:Session = Depends(get_db), data):
        appointment = Appointment(**data.dict())
        db.add(appointment)
        db.commit()
        db.refresh(appointment)
        return appointment