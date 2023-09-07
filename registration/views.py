from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# from .forms import CreateUserForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.forms import inlineformset_factory


# abstract form import
from . forms import CustomeUserCreationForm
# Create your views here.


# REGISTER
def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CustomeUserCreationForm()

        if request.method == 'POST':
            form = CustomeUserCreationForm (request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                success_message = messages.success(request, 'Account successfully created for '+ user)
                return redirect('login')
            # else:
            #     messages.error(request, 'An error occurred during registration')

        context = {'form':form}
        return render(request, 'registration/register.html', context)


# LOGIN
def loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            # username = request.POST.get('username')
            email = request.POST.get('email').lower()
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect!')

        return render(request, 'registration/login.html')

# LOGOUT
def logoutUser(request):
    logout(request)
    return redirect('login')