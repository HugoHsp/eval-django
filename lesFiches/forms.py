from django import forms

from .models import bets


class betsForm(forms.ModelForm):
    model = bets
    fields = ['lastname', 'firstname', 'user_bet', 'user_percent']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
