"""Starter code for the Building REST APIs with FastAPI assignment."""

from fastapi import FastAPI


app = FastAPI(title="Book Catalog API")

books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle", "year": 1962},
]


@app.get("/")
def read_root():
    """Confirm that the API is running."""
    # TODO: Return a JSON message for API visitors.
    pass


@app.get("/books")
def list_books():
    """Return all books in the catalog."""
    return books


# TODO: Add a Pydantic model for validating book data.
# TODO: Add GET, POST, PUT, and DELETE routes for individual books.
