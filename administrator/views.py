from django.shortcuts import render

# Create your views here.

def index_admin(request):
	return render(request, 'admin/inicio_admin.html')