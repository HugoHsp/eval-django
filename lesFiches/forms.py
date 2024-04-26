from django import forms

from .models import bets


class betsForm(forms.ModelForm):
    class Meta:
        model = bets
        fields = ['user_bet', 'user_percent', 'result']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
