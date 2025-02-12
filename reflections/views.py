from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Reflection
from .serializers import ReflectionSerializer

class ReflectionListCreateView(generics.ListCreateAPIView):
    serializer_class = ReflectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Reflection.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
