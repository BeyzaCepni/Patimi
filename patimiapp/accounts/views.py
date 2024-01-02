from django.shortcuts import render, redirect

# Create your views here.

from.forms import LoginForm
from django.contrib.auth import authenticate, login

def login_view(request):
    form = LoginForm(request.templates or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request, user)
        return redirect('homepage')
    return render(request, 'templates/loginPage.html', {'form' : form})

def register_view(request):
    form = RegisterForm(request.templates or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username, password= password)
        login(request, new_user)
        return redirect('homepage')
    return render(request, 'accounts/loginPage.html', {'form': form})
