from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.gerenciador_view, name='gerenciador'),
    path('gerenciador/', views.gerenciador_view, name='gerenciador'),
]
