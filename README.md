REST API для туристических перевалов

Этот проект реализует REST API для управления информацией о туристических перевалах.
Требования

Для корректной работы проекта необходимо наличие следующих компонентов:

    Python 3.8+
    Django 3.2+
    Django REST framework 3.12+

Установка и настройка

    Клонируйте этот репозиторий на свой локальный компьютер.
    Установите необходимые зависимости:

bash

pip install -r requirements.txt

    Выполните миграции:

bash

python manage.py migrate

Методы API
POST /submitData

Метод для добавления новой записи о перевале.
Параметры запроса:

json

{
  "beauty_title": "пер.",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "",
  "add_time": "2021-09-22 13:18:13",
  "user": {
    "email": "qwerty@mail.ru",
    "fam": "Пупкин",
    "name": "Василий",
    "otc": "Иванович",
    "phone": "+7 555 55 55"
  },
  "coords": {
    "latitude": "45.3842",
    "longitude": "7.1525",
    "height": "1200"
  },
  "level": {
    "winter": "",
    "summer": "1А",
    "autumn": "1А",
    "spring": ""
  },
  "images": [
    {"data": "<картинка1>", "title": "Седловина"},
    {"data": "<картинка>", "title": "Подъём"}
  ]
}

Результат метода:

json

{
  "status": 200,
  "message": "Отправлено успешно",
  "id": 42
}

GET /submitData/<id>

Метод для получения информации о перевале по его id.
Результат метода:

json

{
  "id": 42,
  "beauty_title": "пер.",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "",
  "add_time": "2021-09-22 13:18:13",
  "user": {
    "email": "qwerty@mail.ru",
    "fam": "Пупкин",
    "name": "Василий",
    "otc": "Иванович",
    "phone": "+7 555 55 55"
  },
  "coords": {
    "latitude": "45.3842",
    "longitude": "7.1525",
    "height": "1200"
  },
  "level": {
    "winter": "",
    "summer": "1А",
    "autumn": "1А",
    "spring": ""
  },
  "images": [
    {"data": "<картинка1>", "title": "Седловина"},
    {"data": "<картинка>", "title": "Подъём"}
  ],
  "status": "new"
}

PATCH /submitData/<id>

Метод для редактирования существующей записи о перевале в статусе "new".
Параметры запроса:

json

{
  "beauty_title": "пер.",
  "title": "Новое название",
  "other_titles": "Триев",
  "connect": "",
  "add_time": "2021-09-22 13:18:13",
  "level": {
    "winter": "",
    "summer": "1B",
    "autumn": "1B",
    "spring": ""
  },
  "images": [
    {"data": "<новая_картинка>", "title": "Новая фотография"}
  ]
}

Результат метода:

json

{
  "state": 1,
  "message": "Данные успешно отредактированы"
}

GET /submitData/?user__email=<email>

Метод для получения списка данных обо всех объектах, которые пользователь с указанной почтой отправил на сервер.