from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from . models import employees
from . serializers import employeesSerializers

from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status


# Can be applied to get/retrieve all stored data in a database in JSON format
class employeeList(APIView):

    def get(self, request): # GET method
        employees1 = employees.objects.all()
        serializer = employeesSerializers(employees1, many=True)  # serializer is used to take all the objects & convert to JSON. 'many=True' returns more than one JSON object.

        return Response(serializer.data) # returns JSON instead of http response


    def post(self): # POST method
        pass
