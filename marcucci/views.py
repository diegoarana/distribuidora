# -*- coding: UTF-8-*-
from django.shortcuts import render, redirect
from marcucci.form import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
	return render(request, 'distrib/inicio_distribuidor.html')

def login_page(request):
	message = None
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					message = "Te has logueado correctamente"
					return redirect('inicio_distribuidor')
				else:
					message = "Tu usuario esta inactivo"
			else:
				message = "Nombre de usuario y/o contraseña incorrecto"
	else:
		form = LoginForm()
	return render(request, 'login_page.html', {'message':message,'form':form})

def logout_page(request):
	logout(request)
	return redirect('login_page')
