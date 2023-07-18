from django.shortcuts import render
from .models import Boisson
from .serializers import BoissonSerializer
from django.http import JsonResponse
# Create your views here.

def boisson_list(request):
    boisson = Boisson.objects.all()
    serializer=BoissonSerializer(boisson,many=True)
    return JsonResponse({'boisson':serializer.data}, safe=False)

