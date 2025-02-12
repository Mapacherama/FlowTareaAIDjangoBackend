from rest_framework import serializers
from .models import Reflection

class ReflectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reflection
        fields = ['id', 'content', 'created_at']
