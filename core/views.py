from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from .forms import CadastroUsuarioForm, OrcamentoForm
from .models import Orcamento, Projeto, Perfil


# 1. Página Inicial
def index(request):
    return render(request, 'core/index.html')


# 2. Cadastro de Usuário Completo (Com Perfil)
def register_view(request):
    if request.method == 'POST':
        form = CadastroUsuarioForm(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']

            # Verificar se o username já existe
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Esse usuário já existe!')
                return redirect('cadastro')

            # Verificar se o email já existe
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Esse e-mail já está cadastrado!')
                return redirect('cadastro')

            # Criar usuário
            user = User.objects.create_user(
                username=username,
                email=email,
                password=form.cleaned_data['password'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )

            # Atualizar dados do perfil (criado automaticamente pelo signal)
            perfil = user.perfil
            perfil.telefone = form.cleaned_data.get('telefone')
            perfil.idade = form.cleaned_data.get('idade')
            perfil.genero = form.cleaned_data.get('genero')
            if form.cleaned_data.get('foto'):
                perfil.foto = form.cleaned_data.get('foto')
            perfil.save()

            # Login automático após cadastro
            login(request, user)
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('index')
    else:
        form = CadastroUsuarioForm()

    return render(request, 'core/register.html', {'form': form})


# 3. Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'core/login.html', {'form': form})


# 4. Logout
def logout_view(request):
    logout(request)
    return redirect('index')


# 5. Área do Cliente (Protegida)
@login_required
def area_cliente(request):
    orcamentos = Orcamento.objects.filter(cliente=request.user)
    projetos = Projeto.objects.filter(cliente=request.user)

    return render(request, 'core/area_cliente.html', {
        'orcamentos': orcamentos,
        'projetos': projetos
    })


# 6. Solicitar Orçamento (Protegida)
@login_required
def solicitar_orcamento(request):
    if request.method == 'POST':
        form = OrcamentoForm(request.POST)

        if form.is_valid():
            orcamento = form.save(commit=False)
            orcamento.cliente = request.user
            orcamento.save()
            messages.success(request, 'Solicitação enviada com sucesso!')
            return redirect('area_cliente')
    else:
        form = OrcamentoForm()

    return render(request, 'core/solicitar_orcamento.html', {'form': form})