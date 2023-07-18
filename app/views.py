from django.shortcuts import render
from .models import Boisson
from .serializers import BoissonSerializer
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET', 'POST'])
def boisson_list(request):
    if request.method=='GET':
        boisson = Boisson.objects.all()
        serializer=BoissonSerializer(boisson,many=True)
        return JsonResponse({'boisson':serializer.data})

    if request.method=='POST':
        serializer = BoissonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)