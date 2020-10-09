from django.shortcuts import render

# Create your views here.
def vista_base(request):
    return render(request, 'base.html')

def vista_register(request):
    return render(request, 'register.html')

def vista_login(request):
    return render(request, 'login.html')

def vista_index(request):
    return render(request, 'index.html')