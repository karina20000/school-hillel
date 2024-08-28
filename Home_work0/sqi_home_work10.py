import sqlite3

with sqlite3.connect("book_stoore.sqlite3") as connection:
    cursor = connection.cursor()

    query = """
    CREATE TABLE IF NOT EXISTS authors(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     name  TEXT NOT NULL,
     year INTEGER NOT NULL
       )
     """
    cursor.execute(query)
