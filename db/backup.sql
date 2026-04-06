SET client_encoding = 'UTF8';

DROP TABLE IF EXISTS clients CASCADE;
DROP TABLE IF EXISTS workers CASCADE;
DROP TABLE IF EXISTS objects CASCADE;

-- 1. Создаем таблицу объектов с актуальными полями
CREATE TABLE IF NOT EXISTS objects (
    "Object_ID" SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(100),
    price INTEGER,
    rooms INTEGER,
    location VARCHAR(255), 
    image VARCHAR(500),
    badge VARCHAR(100),
    area VARCHAR(50),
    address VARCHAR(500),
    metro VARCHAR(255),
    developer VARCHAR(255),
    status VARCHAR(100)
);

-- 2. Создаем таблицу сотрудников
CREATE TABLE IF NOT EXISTS workers (
    "Worker_ID" SERIAL PRIMARY KEY,
    "full_name" VARCHAR(255) NOT NULL,
    "phone" VARCHAR(20),
    "tg_id" VARCHAR(100)
);

-- 3. Создаем таблицу клиентов
CREATE TABLE IF NOT EXISTS clients (
    "Client_ID" SERIAL PRIMARY KEY,
    "phone" VARCHAR(20),
    "full_name" VARCHAR(255) NOT NULL,
    "Worker_ID" INTEGER REFERENCES workers("Worker_ID"),
    "Object_ID" INTEGER REFERENCES objects("Object_ID"),
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Заполняем объекты (используем только "location")
INSERT INTO objects ("name", "location", "price", "type", "rooms", "area", "address", "badge", "image") 
VALUES 
('ЖК Парадайз', 'Приморский', 15000000, 'Квартиры', 3, '40.3 м²', 'ул. Ленина, 10', 'Проверено', 'house1.jpg'),
('ЖК ПИК', 'Выборгский', 8000000, 'Квартиры', 2, '35.0 м²', 'пр. Мира, 5', 'Новый объект', 'house2.jpg'),
('ЖК Лесной', 'Калининский', 12000000, 'Квартиры', 3, '45.0 м²', 'ул. Лесная, 20', 'Проверено', 'house3.jpg'),
('ЖК Солнечный', 'Фрунзенский', 9000000, 'Квартиры', 2, '30.0 м²', 'пр. Солнечный, 15', 'Новый объект', 'house4.jpg'),
('ЖК Риверсайд', 'Центральный', 20000000, 'Квартиры', 4, '60.0 м²', 'ул. Риверсайд, 1', 'Проверено', 'house5.jpg');

-- 5. Заполняем сотрудников
INSERT INTO workers ("full_name", "tg_id") VALUES 
('Кузнецов Леонид', '718062995'), 
('Пархоменко Максим', '338735156'),
('Капитонов Айдын', '1170769750');