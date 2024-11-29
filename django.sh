#!/bin/bash
echo "Создаем миграции..."
python manage.py makemigrations books
echo ====================================

echo "Запускаем миграции..."
python manage.py migrate
echo ====================================

echo "Запускаем сервер..."
python manage.py runserver 0.0.0.0:8000