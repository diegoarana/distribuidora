from __future__ import unicode_literals
from .camion import Camion
from django.db import models
from django.core.validators import MaxValueValidator 
from .catalog import Catalog

class Stock(models.Model):
	catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name="catalog", null=True)
	amount = models.PositiveIntegerField(validators=[MaxValueValidator(999)], blank = True, null = True)