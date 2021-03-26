from django.forms import ModelForm, Form
from django import forms
from .models import Prikaz

class PrikazForm(ModelForm):
    class Meta:
        model = Prikaz
        fields = ('number', 'date', 'name', 'file', 'note')


class LoginForm(Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'effect-2'}))
    password = forms.CharField(min_length=8, widget=forms.PasswordInput(attrs={'class': 'effect-2'}))
