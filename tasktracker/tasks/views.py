import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def task_api(request):

    if request.method == "GET":
        return JsonResponse({
            "message": "GET request received"
        })

    elif request.method == "POST":

        data = json.loads(request.body)

        return JsonResponse({
            "message": "POST request received",
            "data": data
        })

    elif request.method == "PUT":

        data = json.loads(request.body)

        return JsonResponse({
            "message": "PUT request received",
            "data": data
        })

    elif request.method == "DELETE":

        return JsonResponse({
            "message": "DELETE request received"
        })

    return JsonResponse({
        "error": "Method not allowed"
    }, status=405)