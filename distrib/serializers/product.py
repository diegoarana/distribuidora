from rest_framework import serializers
from distrib.models.product import Product

class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = (
			"id",
			"name",
			"price",
			"amount",
			)