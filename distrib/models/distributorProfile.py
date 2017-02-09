from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator

class DistributorProfile(models.Model):
	address = models.CharField(blank=True, null=True, max_length=30)
	phone = models.BigIntegerField(help_text="(Solamente dígitos)", validators=[MaxValueValidator(999999999999999)], blank = True, null = True)

	def get_address(self):
		return self.address

	def get_phone(self):
		return self.phone

	class Meta:
		abstract = True