"""
Практические задания 21
Лекция 42 - MySQL. Транзакции
Онлайн-магазин книг
Вы создаёте пошагово консольное приложение на Python, работающее с базой данных MySQL и MongoDB. Программа имитирует работу интернет-магазина книг — с регистрацией пользователей, загрузкой и покупкой книг, а также отслеживанием поисковых запросов.
Проект включает в себя следующие этапы:
Создание базы данных и таблиц
Реализация меню магазина с загрузкой данных из файла и регистрацией клиентов
Реализация входа в аккаунт и дополнительного меню клиента
Просмотр и покупка книг
Фиксация покупок в таблице
Фиксация поисков в MongoDB
Анализ самых популярных запросов
Разделение программы на модули

Онлайн-магазин книг. Часть 1

1. Создание книжного магазина

Создайте новую базу данных под названием 010825_bookstore_<your_name>
После этого выполните проверку:
- если база данных успешно создана (или уже существует), выведите сообщение:
  Database 'bookstore' created or already exists.
"""
import mysql.connector
from local_settings import dbconfig_write

db_name = "010825_bookstore_<your_name>"

with mysql.connector.connect(**dbconfig_write) as connection:
    with connection.cursor() as cursor:
        # Шаг 1 — создать базу данных
        cursor.execute(...)               # Создать БД db_name
        cursor.execute("SHOW DATABASES")
        databases = [row[0] for row in cursor]  # Получение списка БД

        if ...:  # проверить, если ваша БД в списке всех БД databases
            print(f"Database '{db_name}' created or already exists.")
        else:
            print("Something went wrong. Database not found.")


# Database '010825_bookstore_BAR' created or already exists.
