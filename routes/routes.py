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
    if not all(key in data for key in ('title', 'author', 'published_year', 'isbn')):
        return jsonify({"error": "Missing required fields"}), 400 # 400 means bad response 
    books[data['isbn']] = data
    return {"message": "book added"}, 201 #201 means created 

@app.route('/books', methods=['GET'])
@swag_from('../swagger/list_books.yml')
def list_books():
    return jsonify(list(books.values())), 200

@app.route('/books/search', methods=['GET'])
@swag_from('../swagger/search_books.yml')
def search_books():
    filters = request.args
    filtered_books = []
    for book in books.values():
        if all(str(book.get(key)) == value for key, value in filters.items()):
            filtered_books.append(book)

    return jsonify(filtered_books), 200

@app.route('/books/<string:isbn>', methods=['DELETE'])
@swag_from('../swagger/delete_books.yml')
def delete_book(isbn):
    if isbn not in books:
        return jsonify({"error": "book not found"}), 404
    del books[isbn]
    return jsonify({"message": "book deleted"}), 200

@app.route('/books/<string:isbn>', methods=['PUT'])
@swag_from('../swagger/update_book.yml')
def update_book(isbn):
    if isbn not in books:
        return jsonify({"error": "book not found"}), 404
    updates = request.get_json()
    books[isbn].update(updates)
    return jsonify({"message": "book updated", "bokk": books[isbn]}), 200