# Django + DRF + PostgreSQL + Docker

## Описание проекта

Простой и базовый API, который предоставляет CRUD-операции над данными через PostgreSQL.

## Данные

В PostgreSQL лежит таблица с книгами (автор, название, год выпуска).

## Запуск приложения через Docker

#### Создание образ Django (DRF):

`docker compose build`

#### Запуск контейнеров Django (DRF) + PostgreSQL:

`docker compose up -d`

#### Создание образов + запуск контейнеров:

`docker compose up --build -d`
