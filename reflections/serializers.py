from rest_framework import serializers
from .models import Reflection

class ReflectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reflection
        fields = ['id', 'content', 'created_at']

    def create(self, validated_data):
        user = self.context['request'].user 
        return Reflection.objects.create(user=user, **validated_data)
