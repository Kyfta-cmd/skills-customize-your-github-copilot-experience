# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with FastAPI to practice defining routes, working with JSON request and response data, and validating user input. You will create an in-memory book catalog that can be explored through FastAPI's interactive documentation.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description

Use the provided starter code to create an API server for a book catalog. Install the dependencies, run the development server, and add a basic route that confirms the API is running.

#### Requirements

Completed program should:

- Create a `FastAPI` application with the title `Book Catalog API`
- Define a `GET /` route that returns a JSON message confirming the API is running
- Define a `GET /books` route that returns the current list of books
- Start successfully with `uvicorn` and display FastAPI's interactive documentation at `/docs`


### 🛠️ Implement Book CRUD Endpoints

#### Description

Add routes that allow clients to create, read, update, and delete books in the in-memory catalog. Each book should have an integer `id`, a `title`, an `author`, and a publication `year`.

#### Requirements

Completed program should:

- Define a Pydantic model for validating book data
- Implement `GET /books/{book_id}` and return a clear `404` response when the book does not exist
- Implement `POST /books` and return the newly created book with a unique `id`
- Implement `PUT /books/{book_id}` to replace an existing book
- Implement `DELETE /books/{book_id}` and return an appropriate success response
- Return JSON responses with meaningful HTTP status codes


### 🛠️ Validate and Test the API

#### Description

Use the automatic documentation at `/docs` or a tool such as `curl` to test successful requests and error cases. Improve the API so invalid data is rejected before it reaches the catalog.

#### Requirements

Completed program should:

- Reject a blank title or author with a validation error
- Reject publication years that are not reasonable four-digit years
- Demonstrate at least one successful request for each CRUD operation
- Demonstrate at least two error cases, including a missing book (`404`)
- Include a short comment or README note describing how to run and test the API

