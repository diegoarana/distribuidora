#-*- coding: UTF-8-*-
from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(
        label=("Nombre de usuario"))
	password = forms.CharField(
        widget=forms.PasswordInput(),
        label=("Contraseña"))