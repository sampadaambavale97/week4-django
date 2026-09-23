from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Task


def home(request):
    return HttpResponse("Welcome to Task Tracker!")


def get_task(request):
    return HttpResponse("GET request received!")


def post_task(request):
    if request.method == "POST":
        return HttpResponse("POST request received!")

    return HttpResponse("""
        <form method="POST">
            <input type="text" name="task" placeholder="Enter task">
            <button type="submit">Send POST</button>
        </form>
    """)


@csrf_exempt
def put_task(request):
    if request.method == "PUT":
        return HttpResponse("PUT request received!")

    return HttpResponse("Please send a PUT request.")


@csrf_exempt
def delete_task(request):
    if request.method == "DELETE":
        return HttpResponse("DELETE request received!")

    return HttpResponse("Please send a DELETE request.")


@csrf_exempt
def task_api(request):

    # GET API
    if request.method == "GET":
        tasks = Task.objects.all()

        data = []

        for task in tasks:
            data.append({
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "completed": task.completed,
            })

        return JsonResponse(data, safe=False)

    # POST API
    if request.method == "POST":
        import json

        data = json.loads(request.body)

        task = Task.objects.create(
            title=data["title"],
            description=data.get("description", ""),
            completed=data.get("completed", False),
        )

        return JsonResponse({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
        }, status=201)

    return JsonResponse({
        "error": "Method not allowed"
    }, status=405)


# PUT and DELETE API
@csrf_exempt
def task_detail_api(request, pk):

    try:
        task = Task.objects.get(id=pk)
    except Task.DoesNotExist:
        return JsonResponse({
            "error": "Task not found"
        }, status=404)

    # PUT API
    if request.method == "PUT":
        import json

        data = json.loads(request.body)

        task.title = data.get("title", task.title)
        task.description = data.get("description", task.description)
        task.completed = data.get("completed", task.completed)

        task.save()

        return JsonResponse({
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "completed": task.completed,
        })

    # DELETE API
    if request.method == "DELETE":
        task.delete()

        return JsonResponse({
            "message": "Task deleted successfully"
        })

    return JsonResponse({
        "error": "Method not allowed"
    }, status=405)