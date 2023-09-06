from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def register(request):
    return render(request, 'registration/register.html')

def login(request):
    return render(request, 'registration/login.html')