from app.db import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, index=True, nullable=False)
    author = db.Column(db.String, index=True, nullable=False)
    year_published = db.Column(db.Integer, index=True)
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Book {self.title!r} by {self.author}>'
