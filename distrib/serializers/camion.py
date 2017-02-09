from rest_framework import serializers
from distrib.models.camion import Camion

class CamionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Camion
		fields = (
			"id",
			"patent",
			"model",
			)