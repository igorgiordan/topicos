from django import forms
from . import models
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
class MatriculaForm(forms.ModelForm):
  datanascimento = forms.DateField(widget=AdminDateWidget)
  class Meta:
    model = models.Aluno
    fields = ['nome', 'pai', 'mae', 'contato', 'datanascimento']