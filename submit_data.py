import requests
import base64
import os

# Определите путь к файлу изображения
file_path = os.path.join(os.path.dirname(__file__), "image1.png")

# Прочитайте файл и преобразуйте его в base64
with open(file_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

# Ваши данные JSON с переменной base64_image
data = {
    "beautyTitle": "перевал",
    "title": "Пхия",
    "add_time": "2023-08-10 12:00:00",
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
    "images": [
        {"data": base64_image, "title": "Седловина"}
    ]
}

# Остальной код для отправки запроса
url = 'http://127.0.0.1:8000/myapp/submit-data/'
headers = {'Content-Type': 'application/json'}
response = requests.post(url, json=data, headers=headers)
print(response.status_code)
print(response.text)