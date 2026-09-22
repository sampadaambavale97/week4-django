# Week 4 - Day 4: Django Models, Migrations and Database

## Objective

The objective of Day 4 was to understand Django models, migrations, and database operations.

In this task, a Task model was created and connected to the Django database.

## Project

Task Tracker - Django Backend

## Technologies Used

- Python
- Django
- SQLite Database
- Django ORM
- Visual Studio Code

## Model Created

A `Task` model was created in:

`taskapp/models.py`

The model contains the following fields:

| Field | Type | Description |
|---|---|---|
| title | CharField | Stores the task title |
| description | TextField | Stores the task description |
| completed | BooleanField | Stores task completion status |

## Model Code

```python
from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title