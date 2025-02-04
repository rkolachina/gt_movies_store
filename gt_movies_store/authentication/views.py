from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render
from django.contrib import auth

# Create your views here.
def register (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            ##return redirect home
        else:
            form = UserCreationForm()
        ##redirect user
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

def login(request):
    template_data = {'title': 'Log In'}

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'GET':
        return render(request, 'authentication/login.html', {'template_data': template_data})

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home')
