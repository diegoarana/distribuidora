from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator
from .profile import Profile

class Sale(models.Model):
	distributor = models.ForeignKey(Profile, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	total_amount = models.PositiveIntegerField(help_text="(Solamente dígitos)", validators=[MaxValueValidator(99999)], blank = True, null = True)

	def __str__(self):
		return self.distributor.name

	def get_date(self):
		return self.date
		
