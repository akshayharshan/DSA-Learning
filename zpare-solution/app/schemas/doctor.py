from pydantic import BaseModel


class Doctor(BaseModel):
    name : str
    specialization : str
    max_daily_slots : int



