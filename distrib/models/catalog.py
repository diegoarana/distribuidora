from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Catalog(models.Model):
	name = models.CharField(max_length=30, blank=True, null=True)
	price = models.FloatField(help_text="(Solamente dígitos)", validators=[MinValueValidator(0.0), MaxValueValidator(999.9)], blank = True, null = True)
	description = models.TextField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.name