# Week 4 - Day 3: HTTP Methods in Django

## Objective

The objective of Day 3 was to understand and implement the basic HTTP methods in Django:

- GET
- POST
- PUT
- DELETE

## Project

Task Tracker - Django Backend

## Technologies Used

- Python
- Django
- HTML
- HTTP Methods
- PowerShell
- Visual Studio Code

## HTTP Methods Implemented

### 1. GET Request

**Endpoint:**

`/get-task/`

**Response:**

`GET request received!`

GET is used to retrieve data from the server.

### 2. POST Request

**Endpoint:**

`/post-task/`

**Response:**

`POST request received!`

POST is used to send or create data on the server.

### 3. PUT Request

**Endpoint:**

`/put-task/`

**Response:**

`PUT request received!`

PUT is used to update existing data on the server.

### 4. DELETE Request

**Endpoint:**

`/delete-task/`

**Response:**

`DELETE request received!`

DELETE is used to remove data from the server.

## Files Modified

### views.py

The following Django views were created:

- `get_task()`
- `post_task()`
- `put_task()`
- `delete_task()`

### urls.py

The following URL routes were added:

```python
path("get-task/", get_task, name="get_task"),
path("post-task/", post_task, name="post_task"),
path("put-task/", put_task, name="put_task"),
path("delete-task/", delete_task, name="delete_task"),