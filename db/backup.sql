SET client_encoding = 'UTF8';

DROP TABLE IF EXISTS clients CASCADE;
DROP TABLE IF EXISTS workers CASCADE;
DROP TABLE IF EXISTS objects CASCADE;

CREATE TABLE objects (
    "Object_ID" SERIAL PRIMARY KEY,
    "name" VARCHAR(255) NOT NULL,
    "district" VARCHAR(100)
);

CREATE TABLE workers (
    "Worker_ID" SERIAL PRIMARY KEY,
    "full_name" VARCHAR(255) NOT NULL,
    "phone" VARCHAR(20),
    "tg_id" VARCHAR(100)
);

CREATE TABLE clients (
    "Client_ID" SERIAL PRIMARY KEY,
    "phone" VARCHAR(20),
    "full_name" VARCHAR(255) NOT NULL,
    "Worker_ID" INTEGER REFERENCES workers("Worker_ID"),
    "Object_ID" INTEGER REFERENCES objects("Object_ID"),
    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ВОЗВРАЩАЕМ ТВОИ ДАННЫЕ
INSERT INTO objects ("name", "district") VALUES 
('ЖК Парадайз', 'Приморский'), 
('ЖК ПИК', 'Выборгский'),
('БЦ Пискаревский', 'Центральный');

INSERT INTO workers ("full_name", "tg_id") VALUES 
('Кузнецов Леонид', '718062995'), 
('Пархоменко Максим', '338735156'),
('Капитонов Айдын', '1170769750'); 