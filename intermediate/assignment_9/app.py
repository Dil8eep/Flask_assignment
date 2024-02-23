#9.Create a RESTful API using Flask to perform CRUD operations on resources like books or movies.
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'  # Use SQLite for simplicity
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)

# Create the database tables

@app.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    book_list = [{'id': book.id, 'title': book.title, 'author': book.author, 'year': book.year} for book in books]
    return jsonify({'books': book_list})

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify({'id': book.id, 'title': book.title, 'author': book.author, 'year': book.year})

@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = Book(title=data['title'], author=data['author'], year=data['year'])
    db.session.add(new_book)
    db.session.commit()
    return jsonify({'message': 'Book added successfully'})

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()
    book.title = data['title']
    book.author = data['author']
    book.year = data['year']
    db.session.commit()
    return jsonify({'message': 'Book updated successfully'})

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted successfully'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0")