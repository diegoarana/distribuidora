from rest_framework import serializers
from distrib.models.client import Client

class ClientSerializer(serializers.ModelSerializer):

	class Meta:
		model = Client
		fields = (
			"id",
			"name",
			"surname",
			"dni",
			"phone",
			"address",
			)