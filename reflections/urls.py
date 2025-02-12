from django.urls import path
from .views import ReflectionListCreateView, ReflectionDetailView

urlpatterns = [
    path('reflections/', ReflectionListCreateView.as_view(), name='reflection-list'),
    path('reflections/<int:pk>/', ReflectionDetailView.as_view(), name='reflection-detail'),
    path("reflections/create", ReflectionListCreateView.as_view(), name="reflection-list-create"),
]