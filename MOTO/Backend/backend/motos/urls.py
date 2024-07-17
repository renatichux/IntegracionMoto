from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_moto, name='crear_moto'),
]
