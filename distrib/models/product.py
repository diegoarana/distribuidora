from __future__ import unicode_literals
from django.db import models

class Product(models.Model):
	name = models.CharField(max_length=30, blank=True, null=True)
	price = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True, null = True)
	description = models.TextField(max_length=200, blank=True, null=True)

	def __str__(self):
		return '%s - $ %s' % (self.name, self.price)