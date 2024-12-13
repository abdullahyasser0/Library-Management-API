from flask import Flask, request, jsonify
from flasgger import swag_from
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

books = {}

@app.route('/books', methods=['POST'])
@swag_from('../swagger/add_book.yml')
def add_book():   
    data = request.get_json()
    if not all(k in data for k in ('title', 'author', 'published_year', 'isbn')):
        return jsonify({"error": "Missing required fields"}), 400
    books[data['isbn']] = data
    return {"message": "Book added"}, 201

@app.route('/books', methods=['GET'])
@swag_from('../swagger/list_books.yml')
def list_books():
    return jsonify(list(books.values())), 200

@app.route('/books/search', methods=['GET'])
@swag_from('../swagger/search_books.yml')
def search_books():
    filters = request.args
    filtered_books = [book for book in books.values() if all(
        str(book.get(k)) == v for k, v in filters.items())]
    return jsonify(filtered_books), 200

@app.route('/books/<string:isbn>', methods=['DELETE'])
@swag_from('../swagger/delete_books.yml')
def delete_book(isbn):
    if isbn not in books:
        return jsonify({"error": "Book not found"}), 404
    del books[isbn]
    return jsonify({"message": "Book deleted"}), 200

@app.route('/books/<string:isbn>', methods=['PUT'])
def update_book(isbn):
    if isbn not in books:
        return jsonify({"error": "Book not found"}), 404
    updates = request.get_json()
    books[isbn].update(updates)
    return jsonify({"message": "Book updated", "book": books[isbn]}), 200