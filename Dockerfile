# Важно взять образ slim (возможно можно и другие, но alpine не будет работать точно, так как нам нужен бинарник из PyPI под названием psycopg2-binary)
FROM python:3.9-slim 

# Запретить Python оставлять byte-code
ENV PYTHONDONTWRITEBYTECODE 1

# Логи при запуске скрипта пойдут напрямую в терминал, они не будут хранится в буфере 
ENV PYTHONUNBUFFERED 1

# Копируем requirements.txt файл в образ
COPY requirements.txt .

# Установка pip зависимостей в образе
RUN pip install -r requirements.txt

# Копируем все оставшиеся файлы проекта в образ 
COPY . .

# Входная точка для запуска программы в образе
ENTRYPOINT ["/django.sh"]
