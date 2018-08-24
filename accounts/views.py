from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm

def index(request):
    context = {
        'pg_title': 'GISPower-accounts',
    }
    return render(request, 'accounts/index.html', context)
from .forms import SignUpForm

def acc_created(request):
    context = {
        'pg_title': 'GISPower-signup_sucess',
    }
    return render(request, 'accounts/acc_created.html', context)

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
        return redirect('/home')
    else:
        form = SignUpForm()
    context = {
        'pg_title': 'GISPower-signup',
        'form': form
    }
    return render(request, 'accounts/signup.html', context)
