#  Django Task Manager

Веб-приложение для управления задачами, разработанное на Django.

##  Функционал

- **CRUD операции**: создание, просмотр, редактирование, удаление задач
- **Фильтрация**: по категории и статусу выполнения
- **Поиск**: по названию задачи
- **Пагинация**: постраничный вывод списка задач
- **Авторизация**: вход/выход пользователей
- **Админка Django**: полное управление данными

##  Технические требования

- Python >= 3.10
- Django >= 4.0
- SQLite (база данных)

##  Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/username/django_task_manager.git
cd django_task_manager
```

### 2. Создать виртуальное окружение

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

### 3. Установить зависимости

```bash
pip install -r requirements.txt
```

### 4. Выполнить миграции

```bash
python manage.py migrate
```

### 5. Создать суперпользователя

```bash
python manage.py createsuperuser
```

### 6. Запустить сервер

```bash
python manage.py runserver
```

Открыть в браузере: http://127.0.0.1:8000

##  Структура проекта

```
django_task_manager/
├── config/                 # Настройки проекта
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── main/                   # Основное приложение
│   ├── migrations/         # Миграции БД
│   ├── templates/          # HTML-шаблоны
│   │   ├── main/
│   │   │   ├── base.html
│   │   │   ├── tasks_list.html
│   │   │   ├── task_detail.html
│   │   │   ├── task_form.html
│   │   │   └── task_confirm_delete.html
│   │   └── registration/
│   │       └── login.html
│   ├── admin.py            # Настройка админки
│   ├── forms.py            # Формы
│   ├── models.py           # Модели (Task, Category)
│   ├── urls.py             # Маршруты приложения
│   └── views.py            # Представления
├── manage.py
├── requirements.txt
└── README.md
```

##  Модели данных

### Category (Категория)
- `name` - название категории

### Task (Задача)
- `title` - название задачи
- `description` - описание
- `created_at` - дата создания
- `deadline` - дедлайн
- `is_done` - статус выполнения
- `category` - категория (ForeignKey)
- `executor` - исполнитель (ForeignKey к User)

##  URL-маршруты

| URL | Описание |
|-----|----------|
| `/` | Список задач |
| `/task/<id>/` | Детали задачи |
| `/create/` | Создание задачи |
| `/update/<id>/` | Редактирование задачи |
| `/delete/<id>/` | Удаление задачи |
| `/toggle/<id>/` | Переключение статуса |
| `/accounts/login/` | Вход |
| `/accounts/logout/` | Выход |
| `/admin/` | Админ-панель Django |

##  Тестовый доступ

- **Логин**: admin
- **Пароль**: admin123

##  Авторы

Сангаджиев Максим, Фофанова Евдокия, Бекетова Дарья

Команда проекта
Сангаджиев Максим: Backend-разработчик (Модели и БД)
Выполненные задачи:

Создание Django-проекта и приложения main
Разработка моделей данных (models.py): модель Category (название категории), модель Task (название, описание, дата создания, дедлайн, статус, категория, исполнитель), настройка связей ForeignKey между моделями
Создание и применение миграций базы данных
Настройка Django Admin (admin.py): регистрация моделей Task и Category, настройка list_display, list_filter, search_fields, добавление возможности редактирования статуса задачи в списке

Файлы: main/models.py, main/admin.py, main/migrations/, config/settings.py

Фофанова Евдокия: Backend-разработчик (Views и формы)
Выполненные задачи:

Разработка представлений (views.py): tasks_list (список задач с фильтрацией, поиском и пагинацией), task_detail (детальный просмотр задачи), task_create (создание новой задачи), task_update (редактирование задачи), task_delete (удаление задачи), task_toggle_status (быстрое переключение статуса)
Создание форм (forms.py): TaskForm с настройкой виджетов Bootstrap
Настройка URL-маршрутов (urls.py)
Реализация авторизации (login/logout)
Защита views декоратором @login_required

Файлы: main/views.py, main/forms.py, main/urls.py, config/urls.py

Бекетова Дарья: Frontend-разработчик и DevOps
Выполненные задачи:

Разработка HTML-шаблонов: base.html (базовый шаблон с навигацией и Bootstrap), tasks_list.html (список задач с фильтрами и пагинацией), task_detail.html (детальный просмотр задачи), task_form.html (форма создания/редактирования), task_confirm_delete.html (подтверждение удаления), login.html (страница входа)
Интеграция Bootstrap 5 для стилизации
Настройка Git-репозитория и GitHub
Создание документации: README.md с инструкцией по запуску, requirements.txt, .gitignore

