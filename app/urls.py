from django.urls import path

from app.templates import views

urlpatterns = [
    path('', views.index, name='index'),
]