from django.urls import path
from . import views
urlpatterns = [
    path('home', views.home, name='home'),
    path('home/<film>', views.home, name='home'),
    path('liste/', views.listeMovies, name='listeFilm'),
]