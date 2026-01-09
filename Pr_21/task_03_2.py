""" 3.2. Регистрация клиента

Добавьте в основное меню пункт, который позволяет пользователю зарегистрироваться в системе.
Пользователь вводит логин, пароль и стартовый баланс;
Логин должен быть уникальным — если такой пользователь уже существует,
регистрация отклоняется "Username already exists.";

Если регистрация прошла успешно — выведите сообщение Registration successful.

Если логин занят — выведите Username already exists.

Пример ввода:
Enter username: alice
Enter password: qwerty
Enter initial balance: 150
Пример вывода:
Registration successful.
"""
def register_user(connection, db_name):
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
        balance = float(input("Enter initial balance: "))
    except ValueError:
        print("Invalid balance.")
        return


        # Проверка: логин занят?


        # Добавляем нового пользователя

    print("Registration successful.")




# Please input 1, 2, 3 or 0:
#     1: Load books from file,
#     2: Register new user,
#     3: Login as user,
#     0: Exit.
# 2
# 2. Register new user
# Enter username: alex
# Enter password: 123
# Enter initial balance: 100
# Registration successful.
#
# Please input 1, 2, 3 or 0:
#     1: Load books from file,
#     2: Register new user,
#     3: Login as user,
#     0: Exit.
