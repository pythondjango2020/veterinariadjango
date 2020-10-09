from django import forms
from .models import *

class citaform(forms.Form):
    name =  forms.CharField(label="Nombre")
    # tipo = 
    # raza = 
    # años = 
    dueño = forms.CharField(label="Dueño")
    consulta = forms.CharField(label="Consulta")
    # fecha = 
    # hora = 