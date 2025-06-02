from django.urls import path
from . import views
from .views import login_view, register_view, home

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('home/', home, name='home'),  # Página principal após login
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  # opcional, mas útil
    path('cadastro/', register_view, name='cadastro'),
    path('detalhesDoArtista/', views.detalhesDoArtista, name='detalhesDoArtista'),
]
