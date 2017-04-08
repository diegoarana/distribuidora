from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator
from .client import Client
from .product import Product

class Borrowed(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

	def __str__(self):
		return '%s - %s' % (self.client.name, self.product.name)