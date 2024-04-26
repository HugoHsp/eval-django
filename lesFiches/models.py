from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    money = models.FloatField(default=10)
    groups = models.ManyToManyField('auth.Group', related_name='custom_user_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_user_permissions')


class Acteur(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    age = models.IntegerField(default=20)
    date_naissance = models.DateField()


class bets(models.Model):
    user_bet = models.IntegerField()
    user_percent = models.FloatField()
    result = models.FloatField()


class Realisateur(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    age = models.IntegerField(default=20)
    date_naissance = models.DateField()


class MovieCard(models.Model):
    titre = models.CharField(max_length=250)
    date_sortie = models.DateField()
    act_prin = models.CharField(max_length=250)
    avis = models.TextField()
    pub = models.BooleanField(default=False)
    note = models.IntegerField(default=0)
    realisateur = models.ForeignKey(Realisateur, on_delete=models.CASCADE, related_name='films')
    acteur = models.ManyToManyField(Acteur, related_name='films')


def __str__(self):
    return self.titre
