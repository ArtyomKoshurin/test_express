# Проект test_library

# Установка и развертывание проекта на локальном сервере
1. Склонируйте репозиторий. 
2. Создайте и активируйте виртуальное окружение
```
python -m venv venv
source venv/Scripts/activate
```
3. Установите зависимости из requirements.txt `pip install -r requirements.txt`
4. В директории /src создайте .env-файл со значениями 
DATABASE_URL=sqlite:///./library.db, JWT_SECRET_KEY=(ваш ключ), JWT_ACCESS_COOKIE_NAME=(рандомное имя), JWT_TOKEN_LOCATION=cookies и JWT_ALGORITHM=HS256. Кроме того, необходимо добавить данные своего smtp-сервера для отправки email писем: EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT


5. В директории src запустите проект python main.py. Тестировать функционал можно как и через swagger, вшитый в FastAPI, так и через Postman.


# Автор:
Кошурин Артём
