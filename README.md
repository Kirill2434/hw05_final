# Финальный проект - Yatube

# Описание проекта

Проект представляет собой социальную сеть для публикации записей в сообществах, с возможностью оставлять комментарии под этими записями. После публикации каждая запись доступна на главной странице, на странице группы и на странице автора. Пользователи могут заходить на чужие страницы и подписываться на понравившихся авторов. Есть возможность модерировать записи и блокировать пользователей.

Стек: Python3, Django 2.2, pytest, unitest, SQlite3, Pillow, sorl-thumbnail.

## Настройка и запуск на ПК

Клонировать репозиторий:

```
git clone https://github.com/Kirill2434/hw05_final
```

Перейти в папку hw05_final/
```
cd hw05_final
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Перейти в папку hw05_final/yatube/
```
cd yatube/
```

Создать и запустить миграции
```
python manage.py makemigrations
python manage.py migrate
```

Запустить локальный сервер
```
python manage.py runserver
```
### Набор доступных адресов:
* ```posts/``` - отображение постов и публикаций.
* ```posts/{id}``` - Получение, изменение, удаление поста с соответствующим id.
* ```posts/{post_id}/comments/``` - Получение комментариев к посту с соответствующим post_id и публикация новых комментариев.
* ```posts/{post_id}/comments/{id}``` - Получение, изменение, удаление комментария с соответствующим id к посту с соответствующим post_id.
* ```posts/groups/``` - Получение описания зарегестрированных сообществ.
* ```posts/groups/{id}/``` - Получение описания сообщества с соответствующим id.
* ```posts/follow/``` - Получение информации о подписках текущего пользователя, создание новой подписки на пользователя.

[![CI](https://github.com/yandex-praktikum/hw05_final/actions/workflows/python-app.yml/badge.svg?branch=master)](https://github.com/yandex-praktikum/hw05_final/actions/workflows/python-app.yml)
