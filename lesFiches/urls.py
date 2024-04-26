from django.urls import path

from . import views
from .views import logout_view
from .views import rules
from .views import user_login
from .views import user_register

urlpatterns = [
    path('home', views.home, name='home'),
    path('home/<film>', views.home, name='home'),
    path('liste/', views.listeMovies, name='listeFilm'),
    path('login/', user_login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', user_register, name='register'),
    path('rules', views.rules, name='rules'),
    path('rules/', rules, name='rules'),
]
