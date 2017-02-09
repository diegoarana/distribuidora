from django.shortcuts import render
from django.db.models import Q

from .models.client import Client

from .serializers.client import ClientSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def client(request):
	query_params = request.query_params.get('q')
	# products = Product.objects.all()
	client = Client.objects.filter(
		Q(surname__icontains=query_params) | \
		Q(dni__startswith=query_params)
		)
	serializer = ClientSerializer(client, many=True)
	return Response(serializer.data)

@api_view(['GET', 'POST'])
def client_list(request):
	""" list all client or create a new client """
	if request.method == 'GET':
		client = Client.objects.all()
		serializer = ClientSerializer(client, many=True)
		return Response(serializer.data)
	elif request.method == 'POST':
		serializer = ClientSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
