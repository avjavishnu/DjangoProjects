from django.urls import path
from .views import get_details

urlpatterns = [
    path("PD", get_details)
]