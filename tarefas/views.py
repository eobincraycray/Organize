from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tarefa
from django.contrib.auth import views as auth_views

@login_required
def lista_tarefas(request):
    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'seutemplate.html', {'tarefas': tarefas})

def gerenciador_view(request):
    tarefas = Tarefa.objects.filter(usuario=request.user)
    return render(request, 'gerenciador.html', {'tarefas': tarefas})
