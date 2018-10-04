from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from datetime import datetime, timedelta

now = datetime.now()

class Aula(models.Model):
 	nome = models.CharField(max_length=150, verbose_name='nome')
 	conteudo = models.TextField(verbose_name='conteúdo')
 	data = models.DateField(auto_now=False, verbose_name='Data')

 	def __str__(self):
 		return self.nome
 	class Meta:
 		verbose_name = 'aula'
 		verbose_name_plural = 'aulas'

class Aluno(models.Model):
	user = models.ForeignKey(User, default=None, on_delete=models.CASCADE, related_name='user1', verbose_name='user')
	nome = models.CharField(max_length=150, verbose_name='nome')
	pai = models.CharField(max_length=150, verbose_name='pai')
	mae = models.CharField(max_length=150, verbose_name='mãe')
	contato = models.CharField(max_length=150, verbose_name='número para contato')
	datanascimento = models.DateField(auto_now=False, verbose_name='data de nascimento')
	def __str__(self):
		return self.nome
	class Meta:
		verbose_name = 'aluno'
		verbose_name_plural = 'alunos'