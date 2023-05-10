from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request, 'nuevoshorizontes/home.html')

def nosotros(request):
    
    return render(request, 'nuevoshorizontes/nosotros.html')

def sedes(request):
    
    return render(request, 'nuevoshorizontes/sedes.html')

def noticias(request):
    
    return render(request, 'nuevoshorizontes/noticias.html')

def login(request):
    
    return render(request, 'nuevoshorizontes/login.html')