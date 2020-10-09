from django import forms
from .models import *

class citaform(forms.Form):
    mascota =  forms.CharField(label="Nombre", required=True)
    tipo = forms.CharField(label="tipo", required=True, widget=forms.Select)
    raza = forms.CharField(label="raza", required=True, widget=forms.Select)
    años = forms.CharField(label="años", required=True, widget=forms.Select)
    dueño = forms.CharField(label="Dueño", required=True)
    descripcion = forms.CharField(label="descripcion", required=True, widget=forms.Textarea)
    fecha = forms.DateField(label="fecha", required=True, widget=forms.TimeInput)
    hora = forms.TimeField(label="hora", required=True)