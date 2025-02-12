from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Reflection
from .serializers import ReflectionSerializer

# ✅ Get a list of reflections & Create a new reflection
class ReflectionListCreateView(generics.ListCreateAPIView):
    serializer_class = ReflectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reflection.objects.filter(user=self.request.user)  # Fetch only user's reflections

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Auto-assign reflection to the logged-in user

# ✅ Get, Update, or Delete a specific reflection by ID
class ReflectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReflectionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Reflection.objects.filter(user=self.request.user)  # Ensure users can only edit their reflections
