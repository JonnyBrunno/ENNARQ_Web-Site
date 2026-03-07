from django.shortcuts import render, redirect
from django.contrib.auth import logout

def index(request):
    return render(request, 'core/index.html')


def register_view(request):
    return render(request, 'core/register.html')


def login_view(request):
    return render(request, 'core/login.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def area_cliente(request):
    return render(request, 'core/area_cliente.html')


def solicitar_orcamento(request):
    return render(request, 'core/solicitar_orcamento.html')