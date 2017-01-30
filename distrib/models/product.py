from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .sale import Sale
from .camion import Camion

class Product(models.Model):
	sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="sale")
	camion = models.ForeignKey(Camion, on_delete=models.CASCADE, related_name="camion")
	name = models.CharField(max_length=30, blank=True, null=True)
	price = models.FloatField(help_text="(Solamente dígitos)", validators=[MinValueValidator(0.0), MaxValueValidator(999.9)], blank = True, null = True)

	def __str__(self):
		return self.name

	def get_name(self):
		self.name

	def get_price(self):
		self.price