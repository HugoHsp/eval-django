from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.template import Template, Context

from lesFiches.models import MovieCard
from .forms import LoginForm
from .forms import betsForm


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
    if request.method == 'POST':
        form = betsForm(request.POST)
        if form.is_valid():
            form.save()
            pass

    return render(request, 'index.html', {'form': form})


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
            return redirect('login')  # Rediriger vers la page après l'inscription
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
