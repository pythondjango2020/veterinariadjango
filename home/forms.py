from django import forms
from .models import *

class citaform(forms.Form):
    mascota =  forms.CharField(label="Nombre", required=True)
    tipo = forms.CharField(label="tipo", required=True)
    raza = forms.CharField(label="raza", required=True)
    años = forms.CharField(label="años", required=True)
    dueño = forms.CharField(label="Dueño", required=True)
    descripcion = forms.CharField(label="descripcion", required=True)
    fecha = forms.DateField(label="fecha", required=True)
    hora = forms.TimeField(label="hora", required=True)