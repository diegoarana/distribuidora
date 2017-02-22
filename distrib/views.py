from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from .models.client import Client

from .serializers.client import ClientSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

#ejemplo jquery UI
import json
from django.http import HttpResponse


# Create your views here.

def homepage(request):
	return render(request, 'index.html')

def inicio_distribuidor(request):
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
	return render(request, 'distrib/client_detail.html', {'client':client})
