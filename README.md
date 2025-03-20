# Проект API для Yatube

Проект представляет собой API для социальной сети **Yatube**, которая позволяет пользователям создавать публикации, комментировать их, объединяться в группы по интересам и подписываться на других авторов. API предоставляет доступ к основным функциям платформы через RESTful интерфейс.

---

## Основные возможности API

1. **Публикации**:
   - Создание, чтение, обновление и удаление постов.
   - Фильтрация постов по группам.
   - Постраничный вывод данных.

2. **Комментарии**:
   - Добавление, просмотр, редактирование и удаление комментариев к постам.

3. **Группы**:
   - Просмотр списка всех групп.
   - Фильтрация постов по группам.

4. **Подписки**:
   - Подписка на авторов.
   - Просмотр ленты подписок.

---

## Как запустить проект

### 1. Клонирование репозитория
Склонируйте репозиторий на ваш локальный компьютер:
```bash
git clone https://github.com/iva-smth/api_final_yatube.git
cd api_final_yatube
```

### 2. Создание и активация виртуального окружения
Создайте виртуальное окружение и активируйте его:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Установка зависимостей
Обновите `pip` и установите зависимости из файла `requirements.txt`:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Выполнение миграций
Примените миграции для базы данных:
```bash
python manage.py migrate
```

### 5. Запуск проекта
Запустите сервер разработки:
```bash
python manage.py runserver
```

Теперь API доступен по адресу: `http://127.0.0.1:8000/`.

---

## Примеры запросов

### 1. Аутентификация

#### Регистрация нового пользователя
```http
POST /api/v1/users/
{
    "username": "new_user",
    "email": "new_user@example.com",
    "password": "secure_password"
}
```

#### Получение токена аутентификации
```http
POST /api/v1/jwt/create/
{
    "username": "new_user",
    "password": "secure_password"
}
```
Ответ:
```json
{
    "access": "your_access_token",
    "refresh": "your_refresh_token"
}
```

### 2. Публикации

#### Создание нового поста
```http
POST /api/v1/posts/
Authorization: Bearer <your_access_token>
{
    "text": "Это мой новый пост!",
    "group": 1
}
```

#### Получение списка постов (постранично)
```http
GET /api/v1/posts/?limit=5&offset=0
```

#### Получение конкретного поста
```http
GET /api/v1/posts/{post_id}/
```

#### Обновление поста
```http
PUT /api/v1/posts/{post_id}/
Authorization: Bearer <your_access_token>
{
    "text": "Обновленный текст поста."
}
```

#### Удаление поста
```http
DELETE /api/v1/posts/{post_id}/
Authorization: Bearer <your_access_token>
```

### 3. Комментарии

#### Добавление комментария к посту
```http
POST /api/v1/posts/{post_id}/comments/
Authorization: Bearer <your_access_token>
{
    "text": "Это мой комментарий!"
}
```

#### Получение списка комментариев к посту
```http
GET /api/v1/posts/{post_id}/comments/
```

#### Удаление комментария
```http
DELETE /api/v1/posts/{post_id}/comments/{comment_id}/
Authorization: Bearer <your_access_token>
```

### 4. Группы

#### Получение списка всех групп
```http
GET /api/v1/groups/
```

#### Получение информации о конкретной группе
```http
GET /api/v1/groups/{group_id}/
```

### 5. Подписки

#### Подписка на автора
```http
POST /api/v1/follow/
Authorization: Bearer <your_access_token>
{
    "following": "author_username"
}
```

#### Получение списка подписок
```http
GET /api/v1/follow/
Authorization: Bearer <your_access_token>
```

---

## Документация

Для просмотра полной документации API перейдите по адресу:
```
http://127.0.0.1:8000/redoc/
```

В документации вы найдете подробное описание всех эндпоинтов, методов, параметров запросов и ответов.

---
