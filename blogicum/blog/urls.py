from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL-адрес '/' вызывает функцию index
]