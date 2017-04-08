from django.db import models
from .client import Client

class Payment(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True, null = True)
	date = models.DateTimeField(auto_now_add = True)