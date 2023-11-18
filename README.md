# Homework__13

Цей проект складається з різних частин, які використовують різні технології, такі як Flask, Django та інші. Нижче наведено інструкції щодо запуску кожної з них.

## FastAPI (main.py)

### Опис
FastAPI використовується для створення REST API.

### Запуск через Docker Compose
1. Переконайтеся, що встановлено Docker та Docker Compose.
2. В кореневій папці проекту виконайте команду:
    ```bash
    docker-compose up --build
    ```

## Django (django_app та django_app_2)

### Опис
Django використовується для створення веб-додатків.

### Запуск через Docker Compose
1. У кожній з папок `django_app` та `django_app_2`:
    - Відкрийте термінал у кожній папці та виконайте команду:
        ```bash
        docker-compose up --build
        ```

## Flask (app та api)

### Опис
Flask використовується для створення веб-додатків та REST API.

### Запуск через Docker Compose

#### API
1. У папці `api`:
    - Відкрийте термінал у папці та виконайте команду:
        ```bash
        docker-compose up --build
        ```

#### Додаток
2. У папці `app`:
    - Відкрийте термінал у папці та виконайте команду:
        ```bash
        docker-compose up --build
        ```

Автор: Наталія
