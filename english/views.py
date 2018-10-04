from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from . import models
from . import forms

class RegisterUser(CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'cadastrousuario.html'

class Home(ListView):
	model = models.Aula
	template_name = 'home.html'

class Roteiro(ListView):
	model = models.Aula
	template_name = 'roteiro.html'
	def get_context_data(self, **kwargs):
		kwargs['aulas'] = models.Aula.objects.all()
		return super(Roteiro, self).get_context_data(**kwargs)

class Matricula(ListView):
	model = models.Aluno
	template_name = 'matricula.html'
	success_url = reverse_lazy('home')
	form_class = forms.MatriculaForm
	
	def form_valid(self, form):
		obj = form.save(commit=False)
		obj.user = models.User.objects.get(id=self.request.user.pk)
		obj.save()
		return HttpResponseRedirect('/')

class Sobre(ListView):
	model = models.Aluno
	template_name = 'sobre.html'

class Contato(ListView):
	model = models.Aluno
	template_name = 'contato.html'