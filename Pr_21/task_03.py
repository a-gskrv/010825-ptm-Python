""" 03. Меню книжного магазина

Сделайте этот файл (task_03.py), главный файлом проекта.
В нём будет размещено основное меню программы.
Каждый раз при запуске этот файл будет
    1. Выполнять код, созданный в предыдущем пункте
    2. В бесконечном цикле запускать пользовательское меню,
     где пользователю будет преложено выбрать 4 цифры:
        1 - загрузить книги из файла (см. пункт 3.1 ниже),
        2 - зарегистрироваться как клиент (см. 3.2),
        3 - войти в свой аккаунт (см. 3.3),
        0 - завершить работу.

Функционал пунктов 1-3 будет выполнен в виде функций.
После выполнения каждого пункта вам необходимо добавить импорт в этот файл (task_03.py).
"""

import mysql.connector
from local_settings import dbconfig_write
from queries import *
from task_03_1 import load_books_from_file
from task_03_2 import register_user
from task_03_3 import try_login, user_menu

db_name = "010825_bookstore_BAR"

with mysql.connector.connect(**dbconfig_write) as connection:
    with connection.cursor() as cursor:
        # Шаг 1 — создать базу данных
        with connection.cursor() as cursor:
            cursor.execute(...)  # Создать БД db_name
            cursor.execute("SHOW DATABASES")
            databases = [row[0] for row in cursor]  # Получение списка БД

            if ...:  # проверить, если ваша БД в списке всех БД databases
                print(f"Database '{db_name}' created or already exists.")
            else:
                print("Something went wrong. Database not found.")

        # Шаг 2 — создать таблицы
        # Готовые запросы есть в queries.py!

        # Вывод списка таблиц
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor]

        print(f"Tables in '{db_name}':")
        for table in tables:
            print(f"- {table}")

        # Бесконечный цикл главного меню
        while True:
            # Текст главного и пользовательского меню есть в queries.py
            pass


# Database '010825_bookstore_BAR' created or already exists.
# Tables in '010825_bookstore_BAR':
# - books
# - users
#
# Please input 1, 2, 3 or 0:
#     1: Load books from file,
#     2: Register new user,
#     3: Login as user,
#     0: Exit.
# 0
# Exiting...
