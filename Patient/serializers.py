from rest_framework import serializers 
from .models import Patient
class TaskSerializer(serializers.ModelSerializer):  
    class Meta:
        model = Patient
        fields = 'all'