# 📘 Assignment: Testing FastAPI APIs with Pytest

## 🎯 Objective

Learn how to test a FastAPI application automatically with pytest and FastAPI's `TestClient`. You will verify successful CRUD operations, validation rules, and error responses without manually clicking through the interactive documentation.

## 📝 Tasks

### 🛠️ Write Basic Endpoint Tests

#### Description

Use the provided test starter file with the completed book catalog API from the previous assignment. Create tests for the root route and the endpoint that lists all books.

#### Requirements

Completed test suite should:

- Create a `TestClient` for the FastAPI application
- Verify that `GET /` returns a `200` status code
- Verify that `GET /books` returns a `200` status code and a JSON list
- Use clear test names that describe the behavior being checked
- Run successfully with pytest


### 🛠️ Test CRUD Behavior

#### Description

Add tests for creating, reading, updating, and deleting a book. Tests should check both status codes and important values in the response body.

#### Requirements

Completed test suite should:

- Test that `POST /books` creates a book and returns its generated `id`
- Test that `GET /books/{book_id}` returns the created book
- Test that `PUT /books/{book_id}` updates the book's details
- Test that `DELETE /books/{book_id}` removes the book
- Confirm that a deleted book can no longer be retrieved


### 🛠️ Test Validation and Error Cases

#### Description

Add tests that prove the API handles invalid input and missing resources safely. Reset shared test data when needed so tests can run independently and repeatedly.

#### Requirements

Completed test suite should:

- Verify that requesting an unknown book returns `404`
- Verify that a blank title or author returns a validation error
- Verify that an invalid publication year is rejected
- Use a pytest fixture or another clear setup strategy to prevent tests from depending on execution order
- Include at least six passing tests covering both successful and unsuccessful requests
