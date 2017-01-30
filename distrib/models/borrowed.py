from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator
from .client import Client

class Borrowed(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	kind = models.CharField(max_length=30, blank=True, null=True)
	total = models.PositiveIntegerField(help_text="(Solamente dígitos)", validators=[MaxValueValidator(999)], blank = True, null = True)

