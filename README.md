# Инструкция по установке и запуску проекта

## Требования

Убедитесь, что у вас установлены следующие компоненты:

- Python 3.x
- pip (установщик пакетов Python)

## Установка зависимостей

Для установки необходимых зависимостей выполните следующую команду:

```
pip install -r requirements.txt
```

## Запуск сервера

Выполните следующую команду, чтобы запустить сервер локально:

```
python3 manage.py runserver
```

Сервер будет доступен по адресу http://127.0.0.1:8000/.

## Запуск тестов

Для запуска тестов, перейдите в директорию "..tests/api_tests/" и выполните следующие команды:

### Запуск самого теста

```
sh run_tests.sh
```


### Получение отчета

```
sh generate_report.sh
```
Эта команда сгенерирует отчет о выполнении тестов в директории test_results.

## Как пользоваться сайтом
1)Создать пользователя

curl --location 'http://127.0.0.1:8000/registration/' \
--header 'Content-Type: application/json' \
--data-raw '{

    "username": "testtest12345",
    "email": "tes12345@yandex.ru",
    "password2": "password123",
    "password": "password123"

}'

2) Получить токен

curl --location 'http://127.0.0.1:8000/token/' \
--header 'Content-Type: application/json' \
--data '{
    "username":"testtest12345",
    "password":"password123"
}'

curl -X GET http://127.0.0.1:8000/api/v1/package/ -H 'Authorization: Token <token>' 

3) Создать подписку


curl --location 'http://127.0.0.1:8000/api/v1/package/' \
--header 'Authorization: Token: f6de769017db7d796f8cce73a93c192aaada1b87' \
--header 'Content-Type: application/json' \
--data '{
    "cam_id": 1,
    "video_color": {
        "brightness": 100, 
        "contrast": 10,
        "hue": 5,
        "saturation": 99
    },
    "channel_no": 2,
    "config_no": 1
}'

4) Получить все подписки пользователя

curl --location 'http://127.0.0.1:8000/api/v1/package/' \
--header 'Authorization: Token: f6de769017db7d796f8cce73a93c192aaada1b87' \
--data ''

5) Получить одну подписку

