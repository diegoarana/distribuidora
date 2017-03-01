from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator
from .product import Product
from .sale_visit import Sale_visit

class Sale_item(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="Product", null=True)
	sale = models.ForeignKey(Sale_visit, on_delete=models.CASCADE, related_name="sale", null=True)
	quantity = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank = True, null = True)

	def __str__(self):
		return '%s - %s' % (self.name, self.quantity)

	def get_name(self):
		self.name

	def get_price(self):
		self.price