# API Automation Testing Framework (Python)

Проект по автоматизации тестирования REST API (JSONPlaceholder).

## 🛠 Стек технологий
- **Python 3.12**
- **Pytest** (тестовый фреймворк)
- **Requests** (HTTP-клиент)
- **Pydantic** (валидация схем ответов)
- **Faker** (генерация тестовых данных)
- **Allure** (красивые отчеты)
- **GitHub Actions** (CI/CD пайплайн)

## 🚀 Как запустить локально
1. Клонировать репозиторий.
2. Установить зависимости: `pip install -r requirements.txt`.
3. Запустить тесты: `pytest --alluredir=allure-results`.
4. Открыть отчет: `allure serve allure-results`.

## 📈 Результаты (CI/CD)
Тесты автоматически запускаются в GitHub Actions при каждом коммите.