# 🎵 Music Catalog API

Современное REST API для управления музыкальным каталогом, построенное на Django REST Framework с интерактивной документацией Swagger.

## 📖 Описание проекта

Music Catalog API - это полнофункциональное веб-приложение для каталогизации музыкальных коллекций. Проект предоставляет удобный REST API для управления исполнителями, альбомами и треками с возможностью интерактивного тестирования через встроенный Swagger UI.

### ✨ Основные возможности

- 🎤 **Управление исполнителями** - создание, просмотр, редактирование и удаление артистов
- 💿 **Каталог альбомов** - полная информация об альбомах с привязкой к исполнителям
- 🎵 **База треков** - детальная информация о песнях с номерами треков
- 📚 **Интерактивная документация** - встроенный Swagger UI для тестирования API
- 🔄 **REST API** - полноценные CRUD операции для всех сущностей
- 🐘 **PostgreSQL** - надежная база данных для хранения информации
- 🐳 **Docker** - контейнеризация для простого развертывания

## 🛠 Технологический стек

- **Backend**: Django 5.2.5, Django REST Framework 3.16.1
- **База данных**: PostgreSQL
- **Документация**: drf-spectacular (OpenAPI 3.0)
- **Контейнеризация**: Docker, Docker Compose
- **Python**: 3.12+

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.12+
- Docker и Docker Compose
- Git

### 1. Клонирование репозитория

```bash
git clone https://github.com/Alvsok/music_data
cd music_data
```

### 2. Запуск через Docker (рекомендуется)

```bash
# Запуск всех сервисов
docker-compose up -d

# Выполнение миграций
docker-compose exec web python manage.py migrate

# Создание суперпользователя (опционально)
docker-compose exec web python manage.py createsuperuser
```

### 3. Локальная установка

```bash
# Создание виртуального окружения
python -m venv venv

# Активация окружения
# На Windows:
venv\Scripts\activate
# На macOS/Linux:
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Настройка переменных окружения
cp .env.example .env
# Отредактируйте .env файл под ваши настройки

# Выполнение миграций
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Запуск сервера разработки
python manage.py runserver
```

## 🔧 Настройка переменных окружения

Создайте файл `.env` в корневой директории проекта:

```bash
# Django
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0

# Database
POSTGRES_DB=music_catalog
POSTGRES_USER=music_user
POSTGRES_PASSWORD=music_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# Internationalization
LANGUAGE_CODE=ru-ru
TIME_ZONE=Europe/Moscow

# Logging
LOG_LEVEL=INFO
```

## 🎯 API Endpoints

### Базовые эндпоинты

| Метод | URL | Описание |
|-------|-----|----------|
| GET | `/api/music/artists/` | Список всех исполнителей |
| POST | `/api/music/artists/` | Создание нового исполнителя |
| GET | `/api/music/artists/{id}/` | Детали исполнителя |
| PUT/PATCH | `/api/music/artists/{id}/` | Обновление исполнителя |
| DELETE | `/api/music/artists/{id}/` | Удаление исполнителя |
| GET | `/api/music/albums/` | Список всех альбомов |
| POST | `/api/music/albums/` | Создание нового альбома |
| GET | `/api/music/albums/{id}/` | Детали альбома |
| PUT/PATCH | `/api/music/albums/{id}/` | Обновление альбома |
| DELETE | `/api/music/albums/{id}/` | Удаление альбома |
| GET | `/api/music/tracks/` | Список всех треков |
| POST | `/api/music/tracks/` | Создание нового трека |
| GET | `/api/music/tracks/{id}/` | Детали трека |
| PUT/PATCH | `/api/music/tracks/{id}/` | Обновление трека |
| DELETE | `/api/music/tracks/{id}/` | Удаление трека |

### Документация и схема

| URL | Описание |
|-----|----------|
| `/swagger/` | 📋 Интерактивная документация Swagger UI |
| `/schema/` | 📄 OpenAPI 3.0 схема в JSON формате |
| `/admin/` | 🛠 Панель администрирования Django |

## 🔍 Интерактивное тестирование в Swagger UI

После запуска приложения откройте браузер и перейдите по адресу: `http://127.0.0.1:8000/swagger/`

### Возможности Swagger UI:

1. **📖 Просмотр документации** - полное описание всех эндпоинтов
2. **🧪 Тестирование API** - кнопка "Try it out" для выполнения запросов
3. **📝 Интерактивные формы** - удобные формы для отправки данных
4. **📊 Примеры ответов** - образцы JSON ответов для каждого эндпоинта
5. **🔗 Связанные данные** - вложенные объекты (альбомы в исполнителях, треки в альбомах)

### Как тестировать:

1. Выберите нужный эндпоинт
2. Нажмите **"Try it out"**
3. Заполните параметры (если требуется)
4. Нажмите **"Execute"**
5. Изучите ответ сервера

## 📊 Структура данных

### Artist (Исполнитель)
```json
{
  "id": 1,
  "name": "The Beatles",
  "albums": [...]
}
```

### Album (Альбом)
```json
{
  "id": 1,
  "artist": 1,
  "title": "Abbey Road",
  "release_year": 1969,
  "tracks": [...]
}
```

### Song (Трек)
```json
{
  "id": 1,
  "album": 1,
  "title": "Come Together",
  "track_number": 1
}
```

## 🔧 Полезные команды

### Django команды

```bash
# Создание и применение миграций
python manage.py makemigrations
python manage.py migrate

# Создание суперпользователя
python manage.py createsuperuser

# Сбор статических файлов
python manage.py collectstatic

# Запуск сервера разработки
python manage.py runserver
```

### Docker команды

```bash
# Запуск сервисов
docker-compose up -d

# Просмотр логов
docker-compose logs -f web

# Остановка сервисов
docker-compose down

# Пересборка контейнеров
docker-compose up -d --build

# Выполнение команд внутри контейнера
docker-compose exec web python manage.py shell
```

## 🧪 Примеры использования

### Создание исполнителя

```bash
curl -X POST "http://127.0.0.1:8000/api/music/artists/" \
  -H "Content-Type: application/json" \
  -d '{"name": "Queen"}'
```

### Создание альбома

```bash
curl -X POST "http://127.0.0.1:8000/api/music/albums/" \
  -H "Content-Type: application/json" \
  -d '{
    "artist": 1,
    "title": "A Night at the Opera",
    "release_year": 1975
  }'
```

### Создание трека

```bash
curl -X POST "http://127.0.0.1:8000/api/music/tracks/" \
  -H "Content-Type: application/json" \
  -d '{
    "album": 1,
    "title": "Bohemian Rhapsody",
    "track_number": 11
  }'
```

## 🐛 Решение проблем

### Проблемы с базой данных

```bash
# Пересоздание базы данных
docker-compose down -v
docker-compose up -d
docker-compose exec web python manage.py migrate
```

### Проблемы с портами

Если порт 8000 занят, измените его в `docker-compose.yml` или используйте другой:

```bash
python manage.py runserver 0.0.0.0:8080
```

### Проблемы с миграциями

```bash
# Сброс миграций
python manage.py migrate --fake music_catalog zero
python manage.py migrate music_catalog
```

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Подробности в файле [LICENSE](LICENSE).

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте ветку для новой функции (`git checkout -b feature/AmazingFeature`)
3. Зафиксируйте изменения (`git commit -m 'Add some AmazingFeature'`)
4. Отправьте в ветку (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📞 Поддержка

Если у вас есть вопросы или предложения, создайте [Issue](https://github.com/yourusername/music_catalog/issues) в репозитории.

---

🎵 **Создано с ❤️ для любителей музыки и качественного кода**