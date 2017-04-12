from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from distrib.models.client import Client

# Create your views here.

@login_required
def bloque_buscar_cliente(request):
	filter_value = request.GET.get('filter', None)
	if filter_value:
		client_list = Client.objects.filter(
		Q(surname__icontains=filter_value) | \
		Q(dni__startswith=filter_value))
		return render(request, 'bloque/bloque_buscar_cliente.html', {'client_list':client_list})
	else:
		client_list = Client.objects.all()
		return render(request, 'bloque/bloque_buscar_cliente.html', {'client_list':client_list})