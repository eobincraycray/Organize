"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # <- ESTE É O IMPORT FALTANDO

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tarefas.urls')),  # Página inicial vindo de 'tarefas'
    path('usuario/', include(('usuario.urls', 'usuario'), namespace='usuario')),
    path('categorias/', include('categoria.urls')),

]
