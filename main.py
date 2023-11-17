from fastapi import FastAPI, Depends, HTTPException
from typing import List, Optional
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Contact, Base
from . import crud, schemas
from .database import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/search/")
async def search_contacts(query: str, db: Session = Depends(get_db)):
    contacts = crud.search_contacts(db, query)
    if not contacts:
        raise HTTPException(status_code=404, detail="Contacts not found")
    return contacts

# Створення бази даних та таблиці контактів
DATABASE_URL = connect(db="mydatabase", host="localhost")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Схема Pydantic для створення контакту
class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: str
    additional_data: Optional[str] = None

# Роут для створення нового контакту
@app.post("/contacts/", response_model=Contact)
def create_contact(contact: ContactCreate):
    db = SessionLocal()
    db_contact = Contact(**contact.dict())
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    db.close()
    return db_contact

# Роут для отримання списку всіх контактів
@app.get("/contacts/", response_model=List[Contact])
def read_contacts(skip: int = 0, limit: int = 10):
    db = SessionLocal()
    contacts = db.query(Contact).offset(skip).limit(limit).all()
    db.close()
    return contacts

# Роут для отримання контакту за ідентифікатором
@app.get("/contacts/{contact_id}", response_model=Contact)
def read_contact(contact_id: int):
    db = SessionLocal()
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    db.close()
    if contact is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact

# Роут для оновлення контакту за ідентифікатором
@app.put("/contacts/{contact_id}", response_model=Contact)
def update_contact(contact_id: int, contact: ContactCreate):
    db = SessionLocal()
    db_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if db_contact is None:
        db.close()
        raise HTTPException(status_code=404, detail="Contact not found")
    for field, value in contact.dict().items():
        setattr(db_contact, field, value)
    db.commit()
    db.refresh(db_contact)
    db.close()
    return db_contact

# Роут для видалення контакту за ідентифікатором
@app.delete("/contacts/{contact_id}", response_model=Contact)
def delete_contact(contact_id: int):
    db = SessionLocal()
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact is None:
        db.close()
        raise HTTPException(status_code=404, detail="Contact not found")
    db.delete(contact)
    db.commit()
    db.close()
    return contact
