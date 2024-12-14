import pytest
from app import app, books

@pytest.fixture(autouse=True)
def clear_books():
    books.clear()

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_add_book(client):
    response = client.post('/books', json={
        "title": "Sample Book",
        "author": "Author Name",
        "published_year": 2021,
        "isbn": "1234567890"
    })
    assert response.status_code == 201
    assert b"book added" in response.data
    assert "1234567890" in books
    assert books["1234567890"]["title"] == "Sample Book"

def test_add_book_missing_fields(client):
    response = client.post('/books', json={
        "title": "Incomplete Book",
        "author": "Author Name"
    })
    assert response.status_code == 400
    assert b"Missing required fields" in response.data

def test_list_books(client):
    client.post('/books', json={
        "title": "Sample Book",
        "author": "Author Name",
        "published_year": 2021,
        "isbn": "1234567890"
    })
    response = client.get('/books')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert data[0]["isbn"] == "1234567890"

def test_search_books(client):
    client.post('/books', json={
        "title": "Searchable Book",
        "author": "Author Name",
        "published_year": 2022,
        "isbn": "1234567891"
    })
    client.post('/books', json={
        "title": "Another Book",
        "author": "Different Author",
        "published_year": 2020,
        "isbn": "1234567892"
    })
    response = client.get('/books/search', query_string={"author": "Author Name"})
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "Searchable Book"

def test_search_books_no_match(client):
    client.post('/books', json={
        "title": "Sample Book",
        "author": "Some Author",
        "published_year": 2021,
        "isbn": "1234567893"
    })
    response = client.get('/books/search', query_string={"author": "Nonexistent Author"})
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_search_books_multiple_filters(client):
    client.post('/books', json={
        "title": "Advanced Search",
        "author": "Jane Doe",
        "published_year": 2021,
        "isbn": "1234567894"
    })
    client.post('/books', json={
        "title": "Another Book",
        "author": "Jane Doe",
        "published_year": 2022,
        "isbn": "1234567895"
    })
    response = client.get('/books/search', query_string={"author": "Jane Doe", "published_year": "2021"})
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "Advanced Search"

def test_delete_book(client):
    client.post('/books', json={
        "title": "Book to Delete",
        "author": "Author Name",
        "published_year": 2023,
        "isbn": "1234567892"
    })
    response = client.delete('/books/1234567892')
    assert response.status_code == 200
    assert b"book deleted" in response.data
    assert "1234567892" not in books

def test_delete_nonexistent_book(client):
    response = client.delete('/books/9999999999')
    assert response.status_code == 404
    assert b"book not found" in response.data

def test_update_book(client):
    client.post('/books', json={
        "title": "Original Book",
        "author": "Original Author",
        "published_year": 2020,
        "isbn": "1234567893"
    })
    response = client.put('/books/1234567893', json={
        "title": "Updated Book",
        "author": "Updated Author"
    })
    assert response.status_code == 200
    assert b"book updated" in response.data
    assert books["1234567893"]["title"] == "Updated Book"
    assert books["1234567893"]["author"] == "Updated Author"

def test_update_nonexistent_book(client):
    response = client.put('/books/9999999999', json={
        "title": "Nonexistent Book",
        "author": "Nonexistent Author"
    })
    assert response.status_code == 404
    assert b"book not found" in response.data
