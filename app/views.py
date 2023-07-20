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
        #Pour avoir une reponse en Json
        #return JsonResponse({'boisson':serializer.data})
        return Response({'boisson':serializer.data})

    if request.method=='POST':
        serializer = BoissonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET', 'PUT','DELETE'])
def boisson_detail(request,id):
    try:
       boisson = Boisson.objects.get(pk=id)
    except Boisson.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = BoissonSerializer(boisson)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer = BoissonSerializer(boisson,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        boisson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
