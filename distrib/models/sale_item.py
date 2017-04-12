from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator
from .product import Product
from .sale_visit import Sale_visit

class Sale_item(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product", null=True, blank=True)
	sale = models.ForeignKey(Sale_visit, on_delete=models.CASCADE, related_name="sale", null=True, blank=True)
	item = models.BooleanField(default=False)
	quantity = models.PositiveSmallIntegerField(validators=[MaxValueValidator(99)], null=True, blank=True)

	def __str__(self):
		return '%s - %s' % (self.product.name, self.quantity)

