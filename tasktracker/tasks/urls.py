from django.urls import path
from .views import task_api


urlpatterns = [
    path("api/tasks/", task_api),
]