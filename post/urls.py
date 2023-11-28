# trilateration_app/urls.py
from django.urls import path
from .views import trilateration_view

urlpatterns = [
    path('trilateration/', trilateration_view, name='trilateration-view'),
]
