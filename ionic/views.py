from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Ionic
from . serializers import IonicSerializer

class IonicList(APIView):
    def get (self, request):
        ionic1 = Ionic.objects.all()
        serializer = IonicSerializer(ionic1, many=True)
        return Response(serializer.data)

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
