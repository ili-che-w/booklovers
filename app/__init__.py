from flask import Flask, render_template, url_for
from flask_migrate import Migrate
from app.db import db
from app.models import Book


app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books')
def books():
    books = Book.query.all()
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run()

