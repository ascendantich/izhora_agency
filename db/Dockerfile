FROM postgres:15

# Указываем автора
LABEL maintainer="my_project"

# Копируем твой дамп в специальную папку. 
# Postgres сам выполнит этот файл при создании базы.
COPY db/backup.sql /docker-entrypoint-initdb.d/

# Оставляем стандартные порты внутри
EXPOSE 5432