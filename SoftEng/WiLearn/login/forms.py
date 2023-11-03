from django import forms
from .models import Teachers


class LoginForm(forms.Form):
    email = forms.CharField(label="Email", widget=forms.TextInput(attrs={'id': "email", 'name': 'email'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'id': "password", 'name': 'password'}))

    class Meta:
        model = Teachers
        fields = ['email', 'password']

