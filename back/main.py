import os
import random
import httpx
from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, cast
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import Optional, List

# Настройки БД
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:admin@db:5432/adminka")
TELEGRAM_BOT_TOKEN = "8568937678:AAHdnyYYHlVq8Yndh_dIjh3yx067_PvNwoo"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- МОДЕЛИ SQLALCHEMY ---

class DBObject(Base):
    __tablename__ = "objects"
    id = Column("Object_ID", Integer, primary_key=True, index=True)
    name = Column("name", String)
    type = Column("type", String)        # Квартиры, Дома, Коммерция
    price = Column("price", Integer)      # Число для фильтрации
    rooms = Column("rooms", Integer)      # Количество комнат
    location = Column("location", String) # Город/Район
    image = Column("image", String)       # Ссылка на картинку
    badge = Column("badge", String)       
    area = Column("area", String)         
    address = Column("address", String)
    metro = Column("metro", String)
    developer = Column("developer", String)
    status = Column("status", String)

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

# Создание таблиц (если их еще нет)
Base.metadata.create_all(bind=engine)

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

from fastapi.staticfiles import StaticFiles

# Добавьте это перед эндпоинтами
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/properties")
def get_properties(
    type: str = "Все объекты",
    budget: str = "Любой",
    rooms: str = "Любое количество",
    location: str = "",
    db: Session = Depends(get_db)
):
    query = db.query(DBObject)

    # 1. Тип объекта
    if type and type != "Все объекты":
        query = query.filter(DBObject.type == type)

    # 2. Бюджет (парсим текст из селекта)
    if budget and budget != "Любой":
        if "До 10 млн" in budget:
            query = query.filter(DBObject.price < 10000000)
        elif "10–20 млн" in budget:
            query = query.filter(DBObject.price >= 10000000, DBObject.price <= 20000000)
        elif "20+" in budget:
            query = query.filter(DBObject.price > 20000000)

    # 3. Количество комнат
    if rooms and rooms != "Любое количество":
        if "3+" in rooms:
            query = query.filter(DBObject.rooms >= 3)
        else:
            try:
                # Извлекаем число из строки "1 комната"
                digit = int(''.join(filter(str.isdigit, rooms)))
                query = query.filter(DBObject.rooms == digit)
            except:
                pass

    # 4. Локация (поиск по подстроке)
    if location:
        query = query.filter(DBObject.location.ilike(f"%{location}%"))

    objs = query.all()
    
    return [
        {
            "id": o.id,
            "title": o.name,
            "price": f"{o.price:,} ₽".replace(",", " ") if o.price else "0 ₽",
            # Добавляем комнаты (важно привести к строке для отображения)
            "rooms": f"{o.rooms} комн." if o.rooms else "Студия",
            # Добавляем плашку (badge)
            "badge": o.badge or "", 
            "image": f"http://localhost:8000/static/{o.image}" if o.image else "",
            "address": o.address or "",
            "status": o.status or "В продаже",
            "area": o.area or ""
        } for o in objs
    ]

# --- ЭНДПОИНТЫ ---

@app.get("/properties") # Изменено с /objects на /properties для соответствия фронтенду
def get_properties(
    type: Optional[str] = "Все объекты",
    budget: Optional[str] = "Любой",
    rooms: Optional[str] = "Любое количество",
    location: Optional[str] = "",
    db: Session = Depends(get_db)
):
    query = db.query(DBObject)

    # Фильтрация по типу
    if type and type != "Все объекты":
        query = query.filter(DBObject.type == type)

    # Фильтрация по бюджету
    if budget and budget != "Любой":
        if budget == "До 10 млн ₽":
            query = query.filter(DBObject.price < 10000000)
        elif budget == "10–20 млн ₽":
            query = query.filter(DBObject.price >= 10000000, DBObject.price <= 20000000)
        elif budget == "20+ млн ₽":
            query = query.filter(DBObject.price > 20000000)

    # Фильтрация по комнатам
    if rooms and rooms != "Любое количество":
        if "3+" in rooms:
            query = query.filter(DBObject.rooms >= 3)
        else:
            try:
                # Извлекаем первое число из строки (например, "1 комната" -> 1)
                num = int(rooms.split()[0])
                query = query.filter(DBObject.rooms == num)
            except (ValueError, IndexError):
                pass

    # Фильтрация по локации (регистронезависимый поиск)
    if location:
        query = query.filter(DBObject.location.ilike(f"%{location}%"))

    objs = query.all()
    
    # Формируем ответ, который ожидает Vue-компонент
    return [
        {
            "id": o.id,
            "title": o.name or "Объект без названия",
            # Форматируем цену с пробелами, только если она есть
            "price": f"{o.price:,} ₽".replace(",", " ") if o.price else "Цена по запросу",
            # Важно: путь к картинке должен быть доступен фронтенду
            "image": o.image if o.image else "https://via.placeholder.com/400x300?text=No+Image",
            "badge": o.badge or "Актуально",
            "area": o.area or "—",
            "address": o.address or "Адрес не указан",
            "metro": o.metro or "",
            "developer": o.developer or "Частное лицо",
            "status": o.status or "В продаже"
        } for o in objs
    ]

# Эндпоинт специально для выпадающего списка в форме (без фильтров)
@app.get("/objects")
def get_objects(db: Session = Depends(get_db)):
    return db.query(DBObject).all()

# 3. Отправка формы
@app.post("/submit-form")
async def create_lead(payload: LeadCreate, db: Session = Depends(get_db)):
    try:
        workers = db.query(DBWorker).all()
        if not workers: 
            raise Exception("В таблице workers нет записей!")
        
        selected_object = db.query(DBObject).filter(DBObject.id == payload.object_id).first()
        object_name = selected_object.name if selected_object else "Неизвестный объект"
        
        target_worker = random.choice(workers)
        
        new_client = DBClient(
            full_name=payload.full_name,
            phone=payload.phone,
            object_id=payload.object_id,
            worker_id=target_worker.id
        )
        db.add(new_client)
        db.commit()

        async with httpx.AsyncClient() as client:
            msg = (
                f"🚀 **Новая заявка!**\n\n"
                f"👤 **Клиент:** {payload.full_name}\n"
                f"📞 **Телефон:** {payload.phone}\n"
                f"📍 **Объект:** {object_name}"
            )
            
            await client.post(
                f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", 
                json={
                    "chat_id": target_worker.tg_id, 
                    "text": msg,
                    "parse_mode": "Markdown"
                }
            )

        return {"status": "success"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))