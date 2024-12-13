import pytest
from routes.routes import app

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
    assert b"Book added" in response.data

def test_list_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
