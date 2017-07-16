from django.db import models
from .client import Client
from django.core.validators import MaxValueValidator

class Payment(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	amount = models.PositiveIntegerField(validators=[MaxValueValidator(999999)], null=False, default=0)
	date = models.DateTimeField(auto_now_add = True)