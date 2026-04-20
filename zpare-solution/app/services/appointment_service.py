from model.doctor import Doctor
from sqlalchemy  import select
from app.respositories.appointment_repo import AppointmentRepository
from app.core.database import get_db
from sqlalchemy.orm import Session

class AppointmentService:

    def __init__(self):

        self.repo = AppointmentRepository()

    def book_appointment(self,db:Session=get_db,data):
        stmt = select(Doctor).where(Doctor.id = data.doctor_id).scalar_one()
        result = db.execute(stmt)

        count = self.repo.count_by_doctor_date(
            db:Session=get_db,data.doctor_id,data.appointment_date
        )

        if count >= result.max_daily_slots
            raise Exception("No slots available")
        
        return self.repo.create( db:Session=get_db,data)