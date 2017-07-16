from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models.client import Client
from .models.product import Product
from .models.borrowed import Borrowed
from .models.profile import Profile

from distrib.forms import SaleVisitForm
from distrib.forms import SaleItemForm
from distrib.forms import PaymentForm

from .serializers.client import ClientSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#ejemplo jquery UI
import json
from django.http import HttpResponse

# Create your views here.
@login_required
def index_distrib(request):
	return render(request, 'distrib/inicio_distribuidor.html')

@api_view(['GET'])
def client(request):

	if request.is_ajax:
		query_params = request.query_params.get('q')
		# products = Product.objects.all()
		client = Client.objects.filter(
		Q(surname__icontains=query_params) | \
		Q(dni__startswith=query_params)
		)

		results=[]

		for cli in client:
			client_json={}
			client_json['label']=cli.surname+" "+cli.name
			client_json['value']=cli.surname +" "+ cli.name
			client_json['id']=cli.id
			results.append(client_json)

		data_json=json.dumps(results)

	else:
		data_json='fail'
	mimetype="application/json"
	return HttpResponse(data_json,mimetype)

	#serializer = ClientSerializer(client, many=True)
	#return Response(serializer.data)

@login_required
def client_detail(request, id):
	client = get_object_or_404(Client, id=id)
	borrow = client.contarPrestados()
	return render(request, 'distrib/client_detail.html', {'client':client, 'borrow':borrow})

@login_required
def detail_borrowed(request, id):
	client = get_object_or_404(Client, id=id)
	borrow = client.contarPrestados()

	#Si la pagina se carga por post, entonces tomo la cantidad de cada input y elimino los respectivos envases
	if request.method == 'POST':

		for key,value in borrow.items():

			cantidad = request.POST[key]
			try:
				cantidad = int(cantidad)
			except Exception as e:
				cantidad = 0
			
			if (cantidad != 0):
				client.devolver_envases(cantidad, key)

		return redirect('client_detail', id=id)
		
	return render(request, 'distrib/detail_borrowed.html', {'borrow':borrow, 'client':client})
	
@login_required
def delete_borrowed(request, id_borrow):
	b = get_object_or_404(Borrowed, id=id_borrow)
	b.delete()
	previous_page = request.META['HTTP_REFERER']
	return redirect(previous_page)


#Mejorar el codigo de esta vista para utilizar con el template sale_visit mejorado
@login_required
def sale_visit(request, id):
	
	client = get_object_or_404(Client, id=id)
	products = Product.objects.all()
	if request.method == 'POST':

		form = SaleVisitForm(request.POST)

		if form.is_valid():
			sale = form.save(commit=False)
			sale.distributor = request.user.usuario
			sale.client = client
			sale.save()
			# si el checkbox de que hay alguien en casa esta marcado
			if sale.succes == True:
				# por cada formulario en la lista de formularios
				for p in products:
					formItem = SaleItemForm(request.POST or None, prefix=p.id)
					item = formItem.save(commit=False)
					# Si la cantidad de un producto es diferente de vacia entonces se le asigna una venta y se guarda
					if (item.quantity != None):
						item.product = p
						item.sale = sale
						item.save()
				# Metodo que calcula el monto total en la venta
				sale.total_amount = sale.calculate_total()
				sale.save()
				# sumo el monto total de la venta a la deuda del cliente
				client.debt += sale.total_amount
				client.save()
				# metodo que asigna envases prestados al cliente dependiendo de la venta
				sale.borrow_products()
		
		return redirect('client_detail', id=id)
	else:

		client = get_object_or_404(Client, id=id)
		products = Product.objects.all()
		# Si la la vista se carga por get entonces inicilizo los formularios vacios
		form = SaleVisitForm()

		# lista de formularios de productos
		listaForm = []
		# agrego un formulario por cada producto
		for p in products:
			item = SaleItemForm(prefix=p.id)
			listaForm.append(item)

	return render(request, 'distrib/sale_visit.html', {'client':client, 'form':form, 'listaForm':listaForm, 'products':products})


def registrarPago(request, id):
	client = get_object_or_404(Client, id=id)

	if request.method == "POST":
		form = PaymentForm(request.POST)

		if form.is_valid(): 
			payment = form.save(commit=False)
			payment.client = client
			payment.save()
			client.debt -= payment.amount 
			client.save()
			return redirect('client_detail', id=id)

	else:
		form = PaymentForm()

	return render(request, 'distrib/registrarPago.html', {'client':client, 'form':form})