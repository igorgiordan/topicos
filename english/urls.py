from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from . import views 

app_name='english'

urlpatterns = [
    path('cadastro/', views.RegisterUser.as_view(), name="cadastro"),
    path('', views.Home.as_view(), name="home"),
    path('sobre/', views.Sobre.as_view(), name="sobre"),
    path('roteiro/', views.Roteiro.as_view(), name="roteiro"),
    path('matricula/', views.Matricula.as_view(), name="matricula"),
    path('contato/', views.Contato.as_view(), name="contato"),
]