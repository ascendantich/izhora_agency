import os
import random
import httpx
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

# Настройки БД
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:admin@db:5432/adminka")
TELEGRAM_BOT_TOKEN = "8568937678:AAHdnyYYHlVq8Yndh_dIjh3yx067_PvNwoo"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- МОДЕЛИ SQLALCHEMY (С точным указанием имен колонок из SQL) ---
class DBObject(Base):
    __tablename__ = "objects"
    id = Column("Object_ID", Integer, primary_key=True, index=True)
    name = Column("name", String)

class DBWorker(Base):
    __tablename__ = "workers"
    id = Column("Worker_ID", Integer, primary_key=True, index=True)
    full_name = Column("full_name", String)
    tg_id = Column("tg_id", String)

class DBClient(Base):
    __tablename__ = "clients"
    id = Column("Client_ID", Integer, primary_key=True, index=True)
    full_name = Column("full_name", String)
    phone = Column("phone", String)
    worker_id = Column("Worker_ID", Integer, ForeignKey("workers.Worker_ID"))
    object_id = Column("Object_ID", Integer, ForeignKey("objects.Object_ID"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

# --- СХЕМЫ PYDANTIC ---
class LeadCreate(BaseModel):
    full_name: str
    phone: str
    object_id: int

# --- ЭНДПОИНТЫ ---
@app.get("/objects")
def get_objects(db: Session = Depends(get_db)):
    # Явно возвращаем структуру, которую ждет фронтенд
    objs = db.query(DBObject).all()
    return [{"Object_ID": o.id, "name": o.name} for o in objs]

@app.post("/submit-form")
async def create_lead(payload: LeadCreate, db: Session = Depends(get_db)):
    try:
        # 1. Получаем список сотрудников
        workers = db.query(DBWorker).all()
        if not workers: 
            raise Exception("В таблице workers нет записей!")
        
        # 2. Находим данные объекта по его ID, который пришел с фронтенда
        selected_object = db.query(DBObject).filter(DBObject.id == payload.object_id).first()
        # Если вдруг объект не найден, подстрахуемся текстом "Неизвестный объект"
        object_name = selected_object.name if selected_object else "Неизвестный объект"
        
        target_worker = random.choice(workers)
        
        # 3. Сохраняем клиента в базу
        new_client = DBClient(
            full_name=payload.full_name,
            phone=payload.phone,
            object_id=payload.object_id,
            worker_id=target_worker.id
        )
        db.add(new_client)
        db.commit()

        # 4. Отправка в Telegram (теперь с Именем объекта)
        async with httpx.AsyncClient() as client:
            msg = (
                f"🚀 **Новая заявка!**\n\n"
                f"👤 **Клиент:** {payload.full_name}\n"
                f"📞 **Телефон:** {payload.phone}\n"
                f"📍 **Объект:** {object_name}"  # <--- Теперь здесь имя, а не ID
            )
            
            await client.post(
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", 
                json={
                    "chat_id": target_worker.tg_id, 
                    "text": msg,
                    "parse_mode": "Markdown" # Чтобы жирный шрифт работал
                }
            )

        return {"status": "success"}
    except Exception as e:
        db.rollback()
        print(f"Ошибка: {e}")
        raise HTTPException(status_code=400, detail=str(e))