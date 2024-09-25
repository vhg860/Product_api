# Product Management API

Это небольшое Django-приложение для управления продуктами через API и фронтенд-страницу. Приложение включает API для создания и получения списка продуктов, а также HTML-страницу с использованием JavaScript для взаимодействия с этим API.

## Функциональность

- API для управления продуктами: создание и получение списка продуктов.
- Фронтенд-страница с формой для добавления нового продукта и таблицей для отображения всех продуктов.
- Используется SQLite как база данных по умолчанию.

## Технологии

- Backend: Django, Django Rest Framework
- Frontend: HTML, JavaScript (Fetch API)
- База данных: SQLite
- Тесты: Pytest

## Установка

1. Клонируйте репозиторий:

```sh
git clone git@github.com:vhg860/Product_api.git
cd 
```
2. Установите зависимости:
```sh
pip install -r requirements.txt
```
3. Выполните миграции для базы данных:
```sh
python manage.py makemigrations
python manage.py migrate
```
4. Запустите сервер разработки:
```sh
python manage.py runserver
```
5. Перейдите по адресу http://127.0.0.1:8000/ для работы с приложением.

## API
### POST /api/products/
- Создает новый продукт.
- Ожидает JSON с полями: name (строка), description (текст), price (десятичное число).
- Пример запроса:
```bash
curl -X POST http://127.0.0.1:8000/api/products/ -H "Content-Type: application/json" -d '{"name": "Product1", "description": "This is a product.", "price": 10.50}'
```
### GET /api/products/
- Возвращает список всех продуктов в формате JSON.
Пример ответа:
```python
[
    {
        "id": 1,
        "name": "Product1",
        "description": "This is a product.",
        "price": 10.50
    }
]
```
## Тестирование
Приложение использует pytest для тестирования. Чтобы запустить тесты, выполните:
```sh
pytest
```
## Фронтенд
HTML-страница включает:
- Форму для создания продукта (поля: название, описание, цена).
- Таблицу для отображения всех созданных продуктов.
- Логику на JavaScript для отправки данных формы на API и обновления списка продуктов без перезагрузки страницы.