from django.urls import path

from .views import optimize_route_view, data_source_table_view

urlpatterns = [
    # Define endpoints

    path('optimize-route/', optimize_route_view, name='optimize_route'),
    path('data-source/', data_source_table_view, name='data_source'),
]
