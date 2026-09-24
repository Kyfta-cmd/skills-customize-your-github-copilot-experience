"""Starter tests for the Testing FastAPI APIs with Pytest assignment.

Save your completed FastAPI application as app.py before running these tests.
Run the suite with: pytest -q
"""

from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_root_route_returns_success():
    """The root route should confirm that the API is running."""
    response = client.get("/")

    assert response.status_code == 200
    # TODO: Assert that the response contains the expected message.


def test_list_books_returns_a_list():
    """The books route should return a JSON list."""
    response = client.get("/books")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


# TODO: Add tests for creating, reading, updating, and deleting a book.
# TODO: Add tests for missing books and invalid request data.
