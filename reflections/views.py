from rest_framework import generics, permissions
from .models import Reflection
from .serializers import ReflectionSerializer

class ReflectionListCreateView(generics.ListCreateAPIView):
    serializer_class = ReflectionSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure user must be logged in

    def get_queryset(self):
        return Reflection.objects.filter(user=self.request.user)  # Show only user's reflections

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Assign the logged-in user automatically