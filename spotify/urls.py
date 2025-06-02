from django.urls import path
from . import views
from .views import login_view, register_view, home

urlpatterns = [
    path('', views.index, name='index'), 
    path('home/', home, name='home'),  
    path('login/', login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  
    path('cadastro/', register_view, name='cadastro'),
    path('detalhesDoArtista/', views.detalhesDoArtista, name='detalhesDoArtista'),
]
