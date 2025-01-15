from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Define endpoints
    path('', include('optimizer.urls')),
]
