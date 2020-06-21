from django.http import JsonResponse
from django.shortcuts import render

# Third party imports
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import PostSerializer
from .models import Post


# The more you go down, the more the code but all achieve the same objective.
'''Method 0-Shortest code'''
class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
        # I don't have to specify any methods since i'm inheriting from 'CreateAPIView'

'''The above class only handles Post request. To add Get request you can do it in two ways'''

# 1st - shortest Code ListCreateAPIView that executes both 'GET' and 'POST' requests.
class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


# 2nd - More Code
class PostCreateView(mixins.ListModelMixin, generics.CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)





'''METHOD 1'''
class PostView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView): # MIXINS should go first
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs): # this func is already build. click on the ListModelMixins. This achieves the same result as the Method 2  with extra func such as pagination    
        return self.list(request, *args, **kwargs)

   
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    # # customize/overide by say send email login
    # def perform_create(self, serializer):
    #     # Send an email logic
    #     serializer.save()





'''METHOD 2'''
# class TestView(APIView):

#     permission_classes = (IsAuthenticated,)

#     def get(self, request, *args, **kwargs):
#         qs = Post.objects.all()
#         # post = qs.first() # To get the 1st instance
#         # serializer = PostSerializer(post)
#         serializer = PostSerializer(qs, many=True) # Here i'm serializing a queryset of the 'POST' model. if passing many queries, add 'many=True'
#         return Response(serializer.data) # Response inherits from 'JsonResponse'

#     def post(self, request, *args, **kwargs):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors)






'''METHOD 3'''
# def test_view(request):
#     data = {
#         'name': 'Martin',
#         'age': 26
#     }
#       # Here i'm passing dict. To pass another type say list. Add 'safe=False' next to data val inside the JsonResponse.
#     return JsonResponse(data)
#        #  You can view the JSON data by runing the server or use the route say, 'curl http://localhost:8000' if the route was set to blank 
