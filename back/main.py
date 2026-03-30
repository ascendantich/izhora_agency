import httpx
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List, Optional

# --- 1. КОНФИГУРАЦИЯ ---
# Замени 'ВАШ_ТОКЕН_БОТА' на токен от @BotFather
TELEGRAM_BOT_TOKEN = "8568937678:AAHdnyYYHlVq8Yndh_dIjh3yx067_PvNwoo"
# Настройки БД: пользователь postgres, пароль admin, порт 5433 (Docker)
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:admin@localhost:5433/local_dev_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- 2. МОДЕЛИ ТАБЛИЦ (согласно твоей схеме) ---
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

# Создание таблиц
Base.metadata.create_all(bind=engine)

# --- 3. СХЕМЫ ДАННЫХ (Pydantic) ---
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

# --- 4. ИНИЦИАЛИЗАЦИЯ ПРИЛОЖЕНИЯ ---
app = FastAPI()

# Настройка CORS для связи с фронтендом на Vue
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Функция для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Функция отправки сообщения в Telegram
async def send_tg_notification(tg_id: str, text: str):
    if not tg_id:
        return
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    async with httpx.AsyncClient() as client:
        try:
            await client.post(url, json={
                "chat_id": tg_id,
                "text": text,
                "parse_mode": "HTML"
            })
        except Exception as e:
            print(f"Ошибка при отправке в Telegram: {e}")

# --- 5. ЭНДПОИНТЫ ---

# Получение списка объектов для выпадающего списка во Vue
@app.get("/objects", response_model=List[ObjectResponse])
def get_objects(db: Session = Depends(get_db)):
    return db.query(Object).all()

# Обработка формы и распределение заявки
@app.post("/submit-form")
async def create_client(client_in: ClientCreate, db: Session = Depends(get_db)):
    # Список ID сотрудников, между которыми делим заявки
    worker_ids = [1, 2, 3] 
    
    # А) Логика Round Robin (определяем очередь)
    last_client = db.query(Client).order_by(desc(Client.Client_ID)).first()
    
    if not last_client or last_client.Worker_ID not in worker_ids:
        next_worker_id = worker_ids[0]
    else:
        try:
            current_index = worker_ids.index(last_client.Worker_ID)
            next_worker_id = worker_ids[(current_index + 1) % len(worker_ids)]
        except ValueError:
            next_worker_id = worker_ids[0]

    # Б) Получаем данные сотрудника и объекта для уведомления
    worker = db.query(Worker).filter(Worker.Worker_ID == next_worker_id).first()
    obj = db.query(Object).filter(Object.Object_ID == client_in.object_id).first()

    # В) Сохраняем нового клиента в базу
    new_client = Client(
        fio=client_in.fio,
        phone=client_in.phone,
        Worker_ID=next_worker_id,
        Object_ID=client_in.object_id
    )
    
    try:
        db.add(new_client)
        db.commit()
        db.refresh(new_client)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail="Ошибка при записи в базу данных")

    # Г) Отправка уведомления в Telegram назначенному сотруднику
    if worker and worker.tg_id:
        msg = (
            f"<b>🚀 Новая заявка!</b>\n\n"
            f"👤 <b>Клиент:</b> {client_in.fio}\n"
            f"📞 <b>Телефон:</b> {client_in.phone}\n"
            f"🏢 <b>Объект:</b> {obj.name if obj else 'Не указан'}"
        )
        await send_tg_notification(worker.tg_id, msg)

    return {
        "status": "success",
        "assigned_worker": worker.fio if worker else next_worker_id,
        "client_id": new_client.Client_ID
    }