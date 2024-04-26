import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from lesFiches.models import MovieCard
from .forms import LoginForm, betsForm


def rules(request):
    return render(request, 'rules.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def home(request):
    if not request.user.is_authenticated:
        return render(request, 'index.html', {'logged': False})

    form = betsForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        result = random.randint(1, 50)  # Exemple de génération aléatoire
        new_bet = form.save(commit=False)
        new_bet.result = result
        new_bet.save()
        return render(request, 'index.html',
                      {'result': result, 'user_percent': form.cleaned_data['user_percent'], 'result_page': True,
                       'logged': True})

    return render(request, 'index.html', {'form': form, 'logged': True})


def listeMovies(request):
    films = MovieCard.objects.all().order_by("date_sortie")
    return render(request, 'list.html', {'films': films})


def listeMoviesTemplate2(request):
    films = MovieCard.objects.all().order_by('date_sortie')
    return render(request, 'list2.html', {'films': films})


def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
