# MyProject

Навчальний Python-проєкт для лабораторної роботи №6: CI/CD на GitHub Actions
(тести, метрики Cloc, SonarQube, Reviewdog, перевірка код-рев'ю).

## Структура

```
.github/workflows/ci.yml   # CI-пайплайн
src/                       # код проєкту
tests/                     # тести pytest
requirements.txt           # залежності
sonar-project.properties   # налаштування SonarQube
setup.py                   # пакування
```

## Локальний запуск

```bash
pip install -r requirements.txt
pytest --junitxml=report.xml --cov=src --cov-report=xml
flake8 src tests
black --check src tests
```

## Секрети GitHub Actions

| Секрет | Призначення |
|--------|-------------|
| `SONAR_TOKEN` | токен проєкту SonarQube |
| `SONAR_HOST_URL` | адреса SonarQube-сервера, доступна з GitHub runner |
