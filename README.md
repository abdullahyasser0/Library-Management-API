# Library-Management-API

This project is a Flask-based RESTful API for managing a collection of books. It includes features like adding, listing, searching, updating, and deleting books. The API also provides interactive Swagger documentation to explore and test endpoints.

---

## Table of Contents
1. [Features](#features)
2. [Prerequisites](#prerequisites)
3. [Building and Running the Docker Container](#building-and-running-the-docker-container)
4. [Accessing the Swagger API Documentation](#accessing-the-swagger-api-documentation)
5. [API Endpoints](#api-endpoints)
6. [Troubleshooting](#troubleshooting)

---

## Features
- Add books to a collection.
- List all books.
- Search for books by query parameters.
- Update details of an existing book.
- Delete books.
- Swagger API documentation for interactive testing.

---

## Prerequisites

Ensure the following tools are installed on your system:
- [Docker](https://www.docker.com/get-started) (version 20.x or higher recommended)
- (Optional) An API testing tool like [Postman](https://www.postman.com/) or [curl](https://curl.se/).

---

## Building and Running the Docker Container

Follow these steps to build and run the Dockerized API:

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone <https://github.com/abdullahyasser0/Library-Management-API.git>
cd <repository-directory>
```

### Step 2: Build the Docker Image
Build the Docker image using the `Dockerfile`:
```bash
docker build -t flask-book-api .
```
- **`-t flask-book-api`**: Tags the image with the name `flask-book-api`.
- **`.`**: Specifies the current directory as the build context.

### Step 3: Run the Docker Container
Run the container with the following command:
```bash
docker run -d -p 5000:5000 flask-book-api
```
- **`-d`**: Runs the container in detached mode (background).
- **`-p 5000:5000`**: Maps port `5000` on your machine to port `5000` in the container.

### Step 4: Verify the Container is Running
Check the running containers:
```bash
docker ps
```
You should see an entry for `flask-book-api` with `5000` exposed.

---

## Accessing the Swagger API Documentation

The API includes Swagger documentation, powered by **Flasgger**, for exploring and testing the endpoints interactively.

### Step 1: Open the Swagger Docs
Once the Docker container is running, open your browser and navigate to:
```
http://localhost:5000/apidocs/
```

### Step 2: Explore Endpoints
- Use the interactive Swagger UI to explore available endpoints.
- Test endpoints directly from the Swagger interface by providing input and submitting requests.

---

## API Endpoints

Here’s a summary of the available endpoints:

1. **Add a Book**
   - **URL**: `/books`
   - **Method**: `POST`
   - **Description**: Add a new book to the collection.

2. **List All Books**
   - **URL**: `/books`
   - **Method**: `GET`
   - **Description**: List all books in the collection.

3. **Search Books**
   - **URL**: `/books/search`
   - **Method**: `GET`
   - **Description**: Search for books using query parameters.

4. **Update a Book**
   - **URL**: `/books/<isbn>`
   - **Method**: `PUT`
   - **Description**: Update an existing book by its ISBN.

5. **Delete a Book**
   - **URL**: `/books/<isbn>`
   - **Method**: `DELETE`
   - **Description**: Delete a book by its ISBN.

For detailed usage of each endpoint, refer to the Swagger documentation.

---

## Troubleshooting

1. **Port Already in Use**
   - If port `5000` is occupied, run the container on a different port:
     ```bash
     docker run -d -p 8080:5000 flask-book-api
     ```
   - Access the API at `http://localhost:8080`.

2. **Cannot Access Swagger Docs**
   - Ensure the container is running:
     ```bash
     docker ps
     ```
   - Check logs for errors:
     ```bash
     docker logs <container-id>
     ```

3. **Build Issues**
   - Ensure your `Dockerfile` is in the correct directory.
   - Verify `requirements.txt` and all necessary files are present.

---

**Happy API Testing!** 🚀
