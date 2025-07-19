from django.shortcuts import render, redirect
from .forms import FormCriarUsuario
from django.contrib import messages

def registrar_usuario(request):
    if request.method == 'POST':
        form = FormCriarUsuario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário criado com sucesso! Faça login.')
            return redirect('login')
    else:
        form = FormCriarUsuario()
    
    return render(request, 'usuarios/registro.html', {'form': form})
