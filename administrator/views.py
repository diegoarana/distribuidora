from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
#ejemplo jquery UI
import json
from django.http import HttpResponse
#restframework
from rest_framework.decorators import api_view
#models
from distrib.models.client import Client
from distrib.models.sale_visit import Sale_visit
from distrib.models.profile import Profile
from distrib.models.product import Product
from distrib.models.payment import Payment
#forms
from administrator.forms import ClientForm
from administrator.forms import ProfileForm
from administrator.forms import AdminProfileForm
from administrator.forms import UserCreationForm
from administrator.forms import ProductForm


@login_required
def index_admin(request):
	return render(request, 'admin/inicio_admin.html')

# ejemplo bloque de agus
@login_required
def buscar_cliente(request):
	filter_value = request.GET.get('filter', None)
	if filter_value:
		client_list = Client.objects.filter(
		Q(surname__icontains=filter_value) | \
		Q(dni__startswith=filter_value))
		return render(request, 'admin/inicio_admin.html', {'client_list':client_list})
	else:
		client_list = Client.objects.all()
		return render(request, 'admin/inicio_admin.html', {'client_list':client_list})

# Views del cliente
@login_required
def new_client(request):
	if request.method == "POST":
		form = ClientForm(request.POST)
		if form.is_valid():
			client = form.save(commit=False)
			client.administrator = request.user.usuario
			client.save()
			return redirect('inicio_administrador')
	else:
		form = ClientForm()
	return render(request, 'admin/new_client.html', {'form':form})

@login_required
def client_detail(request, id):
	client = get_object_or_404(Client, id=id)
	return render(request, 'admin/client_detail.html', {'client':client})

@login_required
def client_sales(request, id):
	client = get_object_or_404(Client, id=id)
	sales = client.get_sales()
	return render(request, 'admin/client_sales.html', {'client':client, 'sales':sales})

@login_required
def client_visits(request, id):
	client = get_object_or_404(Client, id=id)
	visits = client.get_visits()
	return render(request, 'admin/client_visits.html', {'client':client, 'visits':visits})

@login_required
def client_payments(request, id):
	client = get_object_or_404(Client, id=id)
	payments = client.get_payments()
	return render(request, 'admin/client_payments.html', {'client':client, 'payments':payments})

@login_required
def client_borrowed(request, id):
	client = get_object_or_404(Client, id=id)
	borrow = client.get_borrowed()
	return render(request, 'admin/client_borrowed.html', {'borrow':borrow, 'client':client})

@login_required
def client_delete(request, id):
	client = get_object_or_404(Client, id=id)
	client.delete()
	previous_page = request.META['HTTP_REFERER']
	return redirect(previous_page)

# Views de los distribuidores
@login_required
def new_distrib(request):
	if request.user.usuario.is_administrator():
		if request.method == 'POST':
			form_user = UserCreationForm(request.POST or None)
			form_profile = ProfileForm(request.POST or None)
			if form_user.is_valid() and form_profile.is_valid():
				user = form_user.save()
				profile = form_profile.save(commit=False)
				profile.user = user
				profile.user_type = 1
				profile.save()
				return redirect('distrib_list')
			else:
				return render(request, "admin/new_distrib.html", {'form_user':form_user, 'form_profile':form_profile})
		else:
			form_user = UserCreationForm()
			form_profile = ProfileForm()
			return render(request, "admin/new_distrib.html", {'form_user':form_user, 'form_profile':form_profile})
	else:
		return redirect('index')

@login_required
def distrib_list(request):
	d = Profile.objects.all()
	distrib = d.filter(user_type=1)
	return render(request, 'admin/distrib_list.html', {'distrib':distrib})

def distrib_edit(request, id):
	d = get_object_or_404(Profile, user_id=id)
	if request.method == "POST":
		form_profile = ProfileForm(request.POST, instance=d)
		if form_profile.is_valid():
			form_profile.save()
			return redirect('distrib_list')
	else:
		form_profile = ProfileForm(instance=d)
	return render(request, 'admin/distrib_edit.html', {'form_profile':form_profile})

def distribChangePass(request, id):
	d = get_object_or_404(Profile, user_id=id)
	u = d.user
	if request.method == "POST":
		form_user = UserCreationForm(request.POST, instance=u)
		if form_user.is_valid():
			form_user.save()
			return redirect('distrib_list')
	else:
		form_user = UserCreationForm(instance=u)
	return render(request, 'admin/distribChangePass.html', {'form_user':form_user})

# Views de los administradores
@login_required
def new_admin(request):
	if request.user.usuario.is_administrator():
		if request.method == 'POST':
			form_user = UserCreationForm(request.POST or None)
			form_profile = AdminProfileForm(request.POST or None)
			if form_user.is_valid() and form_profile.is_valid():
				user = form_user.save()
				profile = form_profile.save(commit=False)
				profile.user = user
				profile.user_type = 0
				profile.save()
				return redirect('admin_list')
			else:
				# Falta crear el template new_admin.html y poner url
				return render(request, "admin/new_admin.html", {'form_user':form_user, 'form_profile':form_profile})
		else:
			form_user = UserCreationForm()
			form_profile = AdminProfileForm()
			return render(request, "admin/new_admin.html", {'form_user':form_user, 'form_profile':form_profile})
	else:
		return redirect('index')

@login_required
def admin_list(request):
	a = Profile.objects.all()
	admin = a.filter(user_type=0)
	return render(request, 'admin/admin_list.html', {'admin':admin})

@login_required
def admin_edit(request, id):
	a = get_object_or_404(Profile, user_id=id)
	if request.method == "POST":
		form_profile = ProfileForm(request.POST, instance=a)
		if form_profile.is_valid():
			form_profile.save()
			return redirect('admin_list')
	else:
		form_profile = AdminProfileForm(instance=a)
	return render(request, 'admin/admin_edit.html', {'form_profile':form_profile})

def adminChangePass(request, id):
	a = get_object_or_404(Profile, user_id=id)
	u = a.user
	if request.method == "POST":
		form_user = UserCreationForm(request.POST, instance=u)
		if form_user.is_valid():
			form_user.save()
			return redirect('admin_list')
	else:
		form_user = UserCreationForm(instance=u)
	return render(request, 'admin/adminChangePass.html', {'form_user':form_user})

# Views de los productos
@login_required
def new_product(request):
	if request.user.usuario.is_administrator():
		if request.method == 'POST':
			form_product = ProductForm(request.POST or None)
			if form_product.is_valid():
				prod = form_product.save()
				return redirect('products')
			else:
				return render(request, "admin/new_product.html", {'form_product':form_product})
		else:
			form_product = ProductForm()
			return render(request, "admin/new_product.html", {'form_product':form_product})
	else:
		return redirect('index')

@login_required
def products(request):
	products = Product.objects.all()
	return render(request, "admin/products.html", {'products':products})

@login_required
def product_edit(request, id):
	product = get_object_or_404(Product, id=id)
	if request.method == "POST":
		form = ProductForm(request.POST, instance=product)
		if form.is_valid():
			form.save()
			return redirect('products')
	else:
		form = ProductForm(instance=product)
	return render(request, 'admin/product_edit.html', {'form':form})

@login_required
def product_delete(request, id):
	prod = get_object_or_404(Product, id=id)
	prod.delete()
	previous_page = request.META['HTTP_REFERER']
	return redirect(previous_page)

# Views de las ventas y vistas
@login_required
def sales(request):
	sales = Sale_visit.objects.filter(succes=True)
	return render(request, 'admin/sales.html', {'sales':sales})

@login_required
def sale_detail(request, id):
	sale = get_object_or_404(Sale_visit, id=id)
	itemsVenta = sale.get_sale_items()
	return render(request, 'admin/sale_detail.html',{'itemsVenta':itemsVenta, 'sale':sale})

@login_required
def visits(request):
	visits = Sale_visit.objects.filter(succes=False)
	return render(request, 'admin/visits.html', {'visits':visits})