from __future__ import unicode_literals
from django.db import models
from .profile import Profile

class Camion(models.Model):
	distributor = models.OneToOneField(Profile, primary_key=True, on_delete=models.CASCADE)
	patent = models.CharField(max_length=10, blank=True, null=True)
	model = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.model

	def get_patent(self):
		return self.patent

	def get_model(self):
		return self.model