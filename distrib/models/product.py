from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator
from .catalog import Catalog

class Product(models.Model):
	catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name="catalog", null=True)
	quantity = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank = True, null = True)

	def __str__(self):
		return self.catalog.name

	def get_name(self):
		self.name

	def get_price(self):
		self.price