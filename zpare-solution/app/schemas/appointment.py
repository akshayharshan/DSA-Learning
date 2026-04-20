from pydantic import BaseModel
from datetime import date

class Appointment(BaseModel):
    patient_id : int
    doctor_id : int
    appointment_date : date