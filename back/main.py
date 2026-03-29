from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List

# 1. Настройка базы данных
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5433/local_dev_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 2. Модели таблиц (SQLAlchemy)
class Worker(Base):
    __tablename__ = "Сотрудник"
    Worker_ID = Column(Integer, primary_key=True, index=True)
    fio = Column("ФИО", String(255))
    phone = Column("Номер телефона", String(20))
    tg_id = Column("ID Telegram", String(100))

class Object(Base):
    __tablename__ = "Объект"
    Object_ID = Column(Integer, primary_key=True, index=True)
    name = Column("Название объекта", String(255))
    district = Column("Район", String(100))

class Client(Base):
    __tablename__ = "Клиент"
    Client_ID = Column(Integer, primary_key=True, index=True)
    fio = Column("ФИО", String(255))
    phone = Column("Номер телефон", String(20))
    Worker_ID = Column(Integer, ForeignKey("Сотрудник.Worker_ID"))
    Object_ID = Column(Integer, ForeignKey("Объект.Object_ID"))

Base.metadata.create_all(bind=engine)

# 3. Схемы валидации (Pydantic)
class ObjectResponse(BaseModel):
    Object_ID: int
    name: str
    district: str
    class Config:
        from_attributes = True

class ClientCreate(BaseModel):
    fio: str
    phone: str
    object_id: int

# 4. Инициализация приложения (ЭТО ДОЛЖНО БЫТЬ ВЫШЕ ЭНДПОИНТОВ)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 5. Эндпоинты
@app.get("/objects", response_model=List[ObjectResponse])
def get_objects(db: Session = Depends(get_db)):
    return db.query(Object).all()

@app.post("/submit-form")
def create_client(client_in: ClientCreate, db: Session = Depends(get_db)):
    worker_ids = [1, 2, 3] # Твои три сотрудника
    
    # Логика Round Robin
    last_client = db.query(Client).order_by(desc(Client.Client_ID)).first()
    
    if not last_client or last_client.Worker_ID not in worker_ids:
        next_worker_id = worker_ids[0]
    else:
        current_index = worker_ids.index(last_client.Worker_ID)
        next_index = (current_index + 1) % len(worker_ids)
        next_worker_id = worker_ids[next_index]

    new_client = Client(
        fio=client_in.fio,
        phone=client_in.phone,
        Worker_ID=next_worker_id,
        Object_ID=client_in.object_id
    )
    
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    
    return {"status": "success", "assigned_worker_id": next_worker_id}