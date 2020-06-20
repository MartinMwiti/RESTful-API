from django.http import JsonResponse
from django.shortcuts import render

# Third party imports
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'name': 'Martin',
            'age': 26
        }

        return Response(data) # Response inherits from 'JsonResponse'



# def test_view(request):
#     data = {
#         'name': 'Martin',
#         'age': 26
#     }
#     # Here i'm passing dict. To pass another type say list. Add 'safe=False' next to data val inside the JsonResponse.
#     return JsonResponse(data)
#     #  You can view the JSON data by runing the server or use the route say, 'curl http://localhost:8000' if the route was set to blank 
