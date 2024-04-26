import random

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.template import Template, Context

from lesFiches.models import MovieCard, bets
from .forms import LoginForm
from .forms import betsForm

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
    form = None
    if request.method == 'POST' and request.user.is_authenticated:
        if (request.user.is_authenticated):

            form = betsForm(request.POST)
            if form.is_valid():
                result = random.randint(1, 50)  # Exemple de génération aléatoire
                new_bet = bets(
                    user_bet=request.POST['user_bet'],
                    user_percent=request.POST['user_percent'],
                    result=result,
                )
                new_bet.save()
                return render(request, 'index.html',
                              {'result': result, 'user_percent': int(request.POST['user_percent']), 'result_page': True,
                               'logged': True})
                pass
        else:
            return render(request, 'index.html', {'form': form, 'logged': False})

    else:
        return render(request, 'index.html', {'form': form, 'logged': True})


def listeMovies(request):
    films = MovieCard.objects.all().order_by("date_sortie")
    page = """
    {% for film in films %}
    {{film.titre}} <br>
    {% endfor %}
    """
    template = Template(page)
    context = Context({"films": films})
    return render(request, template_name='list.html'
                  , context={'films': films})


def listeMoviesTemplate2(request):
    films = MovieCard.objects.all().order_by('date_sortie')
    return render(request, template_name='list2.html', context={'films': films})


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
