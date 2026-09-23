from django.urls import path
from .views import (
    home,
    get_task,
    post_task,
    put_task,
    delete_task,
    task_api,
    task_detail_api,
)


urlpatterns = [
    path("", home, name="home"),

    # Day 3 APIs
    path("get-task/", get_task, name="get_task"),
    path("post-task/", post_task, name="post_task"),
    path("put-task/", put_task, name="put_task"),
    path("delete-task/", delete_task, name="delete_task"),

    # Day 5 - REST API
    path("api/tasks/", task_api, name="task_api"),

    # Day 5 - PUT & DELETE
    path("api/tasks/<int:pk>/", task_detail_api, name="task_detail_api"),
]