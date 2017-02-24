from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator
from .profile import Profile
from .client import Client
from .product import Product

class Sale_visit(models.Model):
	distributor = models.ForeignKey(Profile, on_delete=models.CASCADE)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	product = models.ManyToManyField(Product)
	succes = models.BooleanField("Hay gente en el domicilio", default=True)
	date = models.DateTimeField(auto_now_add=True)
	total_amount = models.PositiveIntegerField(help_text="(Solamente dígitos)", validators=[MaxValueValidator(99999)], blank = True, null = True)
	comment = models.TextField(blank=True, max_length=100)

	def __str__(self):
		return self.distributor.name

	def get_date(self):
		return self.date

	def get_total(self):
		prod = product.objects.all()
		for p in prod:
			aux = 0
			aux = p.amount * p.catalog.price
			total += aux
		return total		
