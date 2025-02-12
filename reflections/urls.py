from django.urls import path
from .views import ReflectionListCreateView

urlpatterns = [
    path("reflections/", ReflectionListCreateView.as_view(), name="reflection-list-create"),
]