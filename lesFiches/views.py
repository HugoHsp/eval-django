from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from lesFiches.models import MovieCard

def home(request, film = 'qUELQUECHHPOSE'):
    return HttpResponse(f'<h1>Hello World!</h1> {film}')

def listeMovies (request):
    films = MovieCard.objects.all().order_by("date_sortie")
    page = """
    {% for film in films %}
    {{film.titre}} <br>
    {% endfor %}
    """
    template = Template(page)
    context = Context({"films":films})
    return render(request,template_name='list.html'
    ,context ={'films':films })

def listeMoviesTemplate2 (request):
    films = MovieCard.objects.all().order_by('date_sortie')
    return render(request , template_name ='list2.html',context={'films':films })