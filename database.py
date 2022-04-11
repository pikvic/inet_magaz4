import sqlite3
from typing import Iterable


def select(command : str, params : Iterable = tuple()):
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    data = cursor.execute(command, params)
    data = [dict(row) for row in data.fetchall()]
    return data

def get_categories():
    command = "SELECT * FROM categories"
    data = select(command)
    return data

def get_category(cat_id):
    command = "SELECT * FROM categories WHERE id=?"
    data = select(command, (cat_id,))
    return data

def get_items(cat_id):
    command = "SELECT * FROM items WHERE cat_id=?"
    data = select(command, (cat_id,))
    return data
