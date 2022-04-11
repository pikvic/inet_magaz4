import sqlite3


CREATE_CATEGORIES = '''CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY,
    name VARCHAR(60) NOT NULL
)'''

CREATE_ITEMS = '''CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    price INTEGER NOT NULL,
    cat_id INTEGER NOT NULL
)'''

INSERT_CATEGORIES = '''INSERT INTO categories (name) VALUES
    ("Компьютеры"),
    ("Мониторы"),
    ("Молоко")
'''
INSERT_ITEMS = '''INSERT INTO items (name, price, cat_id) VALUES
    ("PC2000", 2000, 1),
    ("Laptop100500", 1000, 1),
    ("Acer 19", 888, 2)
'''

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()
cursor.execute(CREATE_CATEGORIES)
cursor.execute(CREATE_ITEMS)
cursor.execute(INSERT_CATEGORIES)
cursor.execute(INSERT_ITEMS)
conn.commit()