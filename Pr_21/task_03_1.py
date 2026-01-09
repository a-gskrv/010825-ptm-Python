""" 03. Меню книжного магазина

3.1. Загрузка книг из файла

Добавьте пункт меню, который позволяет загрузить список книг из файла.
Каждая строка файла содержит: название, автор, цена, количество;
Если книга с таким названием и автором уже есть — обновляется количество;
Если такой книги нет — создаётся новая запись;
После завершения загрузки выводится количество обработанных книг.

Пример файла:
1984,George Orwell,8.99,5
Brave New World,Aldous Huxley,9.50,3
Пример вывода:
2 books loaded.
"""


def load_books_from_file(filename, connection, db_name):
    added = 0  # подсчитываем кол-во добавленных книг
    with ... as file:   # открываем файл
        pass

        for line in file:


            if ...:
                continue  # пропускаем некорректные строки файла



                # Проверка: есть ли такая книга


                # Если есть - добавляем кол-во из файла к тому, что уже есть

                # Если нет - добавляем книгу и увеличиваем счётчик добавленных
            added += 1

    print(f"{added} books loaded.")





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
# 1
#
# --- Bookstore Menu ---
# 1. Load books from file
# Enter file name: books.csv
# 12 books loaded.
#
# Please input 1, 2, 3 or 0:
#     1: Load books from file,
#     2: Register new user,
#     3: Login as user,
#     0: Exit.
