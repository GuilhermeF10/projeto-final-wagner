from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import LoginForm, RegisterForm

User = get_user_model()

def index(request):
    """
    Página inicial pública.
    """
    return render(request, 'spotify/index.html')


def home(request):
    """
    Página principal após login.
    """
    return render(request, 'spotify/home.html')


def detalhesDoArtista(request):
    return render(request, 'spotify/detalhesDoArtista.html')


def login_view(request):
    """
    Exibe o formulário de login e faz a autenticação.
    Se credenciais estiverem corretas, redireciona para 'home'.
    """
    form = LoginForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        usuario = form.cleaned_data['username']
        senha = form.cleaned_data['password']
        user = authenticate(request, username=usuario, password=senha)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            form.add_error(None, 'Usuário ou senha inválidos.')
    return render(request, 'spotify/login.html', {'form': form})


def logout_view(request):
    """
    Encerra a sessão do usuário e redireciona para a página de login.
    """
    logout(request)
    return redirect('login')


def register_view(request):
    """
    Exibe o formulário de cadastro (RegisterForm).
    Se for POST e válido, salva o novo usuário, faz login automático e redireciona para 'home'.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Criptografa a senha
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'spotify/cadastro.html', {'form': form})

