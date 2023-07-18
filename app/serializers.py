from rest_framework import serializers
from .models import Boisson

class BoissonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boisson
        fields = ['id','name','description']