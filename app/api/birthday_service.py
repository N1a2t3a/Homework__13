from sqlalchemy.orm import Session
from datetime import date, timedelta
from .models import BaseModel

def get_upcoming_birthdays(db: Session, days=7):
    today = date.today()
    end_date = today + timedelta(days)
    birthdays = db.query(BaseModel).filter(
        BaseModel.birthday >= today, BaseModel.birthday <= end_date
    ).all()
    return birthdays