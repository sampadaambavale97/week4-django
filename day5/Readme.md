# Week 4 - Day 5: REST API and JSON

## Objective

The objective of Day 5 was to understand how to create and test REST APIs using Django and JSON.

In this task, CRUD-style API operations were implemented using Django's `JsonResponse`.

---

## Project

**Project Name:** Task Tracker

**Technology Used:**
- Python
- Django
- SQLite
- JSON
- PowerShell

---

## Topics Covered

- REST API basics
- JSON data
- Django `JsonResponse`
- GET API
- POST API
- PUT API
- DELETE API
- API testing using PowerShell

---

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/tasks/` | Get all tasks |
| POST | `/api/tasks/` | Create a new task |
| PUT | `/api/tasks/<id>/` | Update a task |
| DELETE | `/api/tasks/<id>/` | Delete a task |

---

## 1. GET API

The GET API retrieves all tasks from the database.

### Endpoint

```text
GET /api/tasks/