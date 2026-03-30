FROM python:3.11-slim

WORKDIR /app

# Сначала копируем зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем всё содержимое папки back ПРЯМО в /app
COPY . .

# Проверка для отладки (выведет список файлов в лог при сборке)
RUN ls -la /app

EXPOSE 8000

# Запускаем uvicorn. 
# "main:app" означает: ищи файл main.py и в нем объект app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]