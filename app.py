from flask import Flask, render_template, abort, request, redirect, session
from flask.helpers import url_for
from database import get_categories, get_items, get_category, insert, select

app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.get("/")
def index():
    username = session.get("username", None)
    categories = get_categories()
    return render_template('index.html', username=username, categories=categories)

@app.get("/<int:cat_id>")
def category(cat_id):
    username = session.get("username", None)
    category = get_category(cat_id)
    if not category:
        abort(404)
    category = category[0]
    items = get_items(cat_id)
    return render_template('category.html', username=username, category=category, items=items)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        username = session.get("username", None)
        if username:
            return redirect(url_for('index'))
        return render_template('login.html')
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"] 
        command = '''SELECT * FROM users WHERE username = ?'''
        users = select(command, (username,))
        if not users:
            command = '''INSERT INTO users (username, password) VALUES (?, ?)'''
            insert(command, (username, password))
            # login
            session['username'] = username
            return redirect(url_for('index'))
        else:
            if users[0]["password"] == password:
                # login       
                session['username'] = username
                return redirect(url_for('index'))
            else:
                # show_error
                return redirect(url_for('index'))
@app.get("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))