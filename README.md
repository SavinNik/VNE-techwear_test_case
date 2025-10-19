# VNE - Интернет-магазин techwear-одежды

## Требования
- Python 3.9+
- PostgreSQL 13+
- Docker (опционально, для запуска через контейнеры)
- pip (менеджер пакетов Python)

## Установка

1. **Клонирование репозитория**
   ```bash
   git clone <ваш-репозиторий>
   cd VNE_techwear
   ```

2. **Создание виртуального окружения**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # для Linux/Mac
   # ИЛИ
   .venv\Scripts\activate    # для Windows
   ```

3. **Установка зависимостей**
   ```bash
   pip install -r requirements.txt
   ```

4. **Настройка переменных окружения**
   Создайте файл `.env` в корне проекта и заполните его по примеру `.env.example`.

## Настройка базы данных

1. Создайте базу данных в PostgreSQL.
2. Примените миграции:
   ```bash
   alembic upgrade head
   ```

## Запуск приложения

### Разработка
```bash
uvicorn api.api_main:app --reload
```

### Запуск в Docker
```bash
docker compose up --build
```

## Доступ к API
После запуска приложение будет доступно по адресу: [http://localhost:8000](http://localhost:8000)

Документация API:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)



