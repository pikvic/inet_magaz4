from flask import Flask, render_template, abort
from database import get_categories, get_items, get_category

app = Flask(__name__)

@app.get("/")
def index():
    categories = get_categories()
    return render_template('index.html', categories=categories)

@app.get("/<int:cat_id>")
def category(cat_id):
    category = get_category(cat_id)
    if not category:
        abort(404)
    category = category[0]
    items = get_items(cat_id)
    return render_template('category.html', category=category, items=items)