from django.shortcuts import render
from django.http import JsonResponse


def test_view(request):
    data = {
        'name': 'Martin',
        'age': 26
    }
    # Here i'm passing dict. To pass another type say list. Add 'safe=False' next to data val inside the JsonResponse.
    return JsonResponse(data)
    #  You can view the JSON data by runing the server or use the route say, 'curl http://localhost:8000' if the route was set to blank 
