from django.urls import path
from login import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacto/',views.contacto, name='contacto'),
]