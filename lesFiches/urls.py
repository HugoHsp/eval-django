from django.urls import path

from . import views
from .views import user_login, user_logout
from .views import user_register
from .views import rules

urlpatterns = [
    path('home', views.home, name='home'),
    path('home/<film>', views.home, name='home'),
    path('liste/', views.listeMovies, name='listeFilm'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('rules', views.rules, name='rules'),
    path('rules/', rules, name='rules'),  # L'URL pour la page "rules"
]