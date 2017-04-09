from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from .models.client import Client
from .models.product import Product
from .models.borrowed import Borrowed
from .models.profile import Profile

from distrib.forms import SaleVisitForm
from distrib.forms import SaleItemForm

from .serializers.client import ClientSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#ejemplo jquery UI
import json
from django.http import HttpResponse


# Create your views here.

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

def client_detail(request, id):
	client = get_object_or_404(Client, id=id)
	borrow = client.get_borrowed()
	return render(request, 'distrib/client_detail.html', {'client':client, 'borrow':borrow})

def detail_borrowed(request, id):
	client = get_object_or_404(Client, id=id)
	borrow = client.get_borrowed()
	return render(request, 'distrib/detail_borrowed.html', {'borrow':borrow, 'client':client})

def delete_borrowed(request, id_borrow):
	b = get_object_or_404(Borrowed, id=id_borrow)
	b.delete()
	previous_page = request.META['HTTP_REFERER']
	return redirect(previous_page)


def sale_visit(request, id):
	client = get_object_or_404(Client, id=id)
	products = Product.objects.all()
	if request.method == 'POST':
		#Inicializo los formularios de cada item
		formItem1 = SaleItemForm(request.POST or None, prefix="item1")
		formItem2 = SaleItemForm(request.POST or None, prefix="item2")
		formItem3 = SaleItemForm(request.POST or None, prefix="item3")
		formItem4 = SaleItemForm(request.POST or None, prefix="item4")

		form = SaleVisitForm(request.POST)

		if form.is_valid():
			sale = form.save(commit=False)
			sale.distributor = request.user.usuario
			sale.client = client
			sale.save()

			succes = request.POST.get('succes', False)
			if succes == "on":

				item1 = formItem1.save(commit=False)
				item2 = formItem2.save(commit=False)
				item3 = formItem3.save(commit=False)
				item4 = formItem4.save(commit=False)
				# agarro los valores de los checkbox y los productos para verificar
				it1 = request.POST.get('item1-item', False)
				it2 = request.POST.get('item2-item', False)
				it3 = request.POST.get('item3-item', False)
				it4 = request.POST.get('item4-item', False)
				prod1 = request.POST.get('item1-product')
				prod2 = request.POST.get('item2-product')
				prod3 = request.POST.get('item3-product')
				prod4 = request.POST.get('item4-product')
				
				if it1 == "on":
					if prod1:
						item1.sale = sale
						item1.save()
				if it2 == "on":
					if prod2:
						item2.sale = sale
						item2.save()
				if it3 == "on":
					if prod3:
						item3.sale = sale
						item3.save()
				if it4 == "on":
					if prod4:
						item4.sale = sale
						item4.save()

				sale.total_amount = sale.calculate_total()
				sale.save()
				# funcion que asigna envases prestados al cliente dependiendo de la venta
				sale.borrow_products()

			return redirect('inicio_distribuidor')
	else:
		form = SaleVisitForm()
		formItem1 = SaleItemForm(prefix="item1")
		formItem2 = SaleItemForm(prefix="item2")
		formItem3 = SaleItemForm(prefix="item3")
		formItem4 = SaleItemForm(prefix="item4")

	return render(request, 'distrib/sale_visit.html', {'client':client, 'form':form, 'formItem1':formItem1,'formItem2':formItem2,'formItem3':formItem3, 'formItem4':formItem4, 'products':products})


