from django.shortcuts import render
from .forms import citaform

# Create your views here.
def vista_base(request):
    return render(request, 'base.html')

def vista_register(request):
    return render(request, 'register.html')

def vista_login(request):
    return render(request, 'login.html')

def vista_index(request):
    return render(request, 'index.html')

def vista_formulario(request):
    cita_form = citaform()
    return render(request, 'formulario.html',{'form':cita_form})