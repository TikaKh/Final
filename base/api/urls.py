from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('travels/', views.get_travels),
    path('travels/<str:id>', views.get_travel),
]