from django.http import JsonResponse
from django.shortcuts import render

# Third party imports
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import PostSerializer
from .models import Post


class TestView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        qs = Post.objects.all()
        # post = qs.first() # To get the 1st instance
        # serializer = PostSerializer(post)
        serializer = PostSerializer(qs, many=True) # Here i'm serializing a queryset of the 'POST' model. if passing many queries, add 'many=True'
        return Response(serializer.data) # Response inherits from 'JsonResponse'

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)











# def test_view(request):
#     data = {
#         'name': 'Martin',
#         'age': 26
#     }
#     # Here i'm passing dict. To pass another type say list. Add 'safe=False' next to data val inside the JsonResponse.
#     return JsonResponse(data)
#     #  You can view the JSON data by runing the server or use the route say, 'curl http://localhost:8000' if the route was set to blank 
