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
