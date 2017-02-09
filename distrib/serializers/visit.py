from rest_framework import serializers
from distrib.models.visit import Visit

class VisitSerializer(serializers.ModelSerializer):

	class Meta:
		model = Visit
		fields = (
			"succes",
			"date",
			"comment",
			)