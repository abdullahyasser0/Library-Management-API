from flask import Flask, request, jsonify

app = Flask(__name__)
books = {}


@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    if not all(k in data for k in ('title', 'author', 'published_year', 'isbn')):
        return jsonify({"error": "Missing required fields"}), 400
    books[data['isbn']] = data
    return jsonify({"message": "Book added", "book": data}), 201

@app.route('/books', methods=['GET'])
def list_books():
    return jsonify(list(books.values())), 200

@app.route('/books/search', methods=['GET'])
def search_books():
    filters = request.args
    filtered_books = [book for book in books.values() if all(
        str(book.get(k)) == v for k, v in filters.items())]
    return jsonify(filtered_books), 200

@app.route('/books/<string:isbn>', methods=['DELETE'])
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
