""" 6. Фиксация поисков в MongoDB
Добавьте сохранение всех поисковых запросов по книгам в MongoDB для последующего анализа.
Используйте подключение:
from pymongo import MongoClient

Используйте базу ich_edit, коллекцию bookstore_logs_searches;
При каждом поиске сохраняйте текст запроса — то, что ввёл пользователь;
Пример записи в MongoDB:
{ "query": "book_name" }

⚠️  Можно подключиться к MongoDB как предложено здесь:
    - подключение идёт вмести с импортом функции log_search_query
    - для учебного проекта это вполне нормально.
    Но более правильным считается подключение в main.py вместе с подключением к MySQL
"""



# (доработка search_books_by_title):
from pymongo import MongoClient
from local_settings import MONGODB_URL_WRITE

mongo_client = MongoClient(MONGODB_URL_WRITE)
searches_collection = mongo_client["ich_edit"]["010825_bookstore_logs_searches_<your_name>"]

def log_search_query(query: str):
    pass


# добавляем вызов функции log_search_query в функцию search_books_by_title()


# Обязательно проверьте: посл ввода пользователем поискового запроса книги по названию,
# этот запрос должен добавиться в коллекцию  010825_bookstore_logs_searches_BAR