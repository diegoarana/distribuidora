from __future__ import unicode_literals
from django.db import models
from .profile import Profile

class Zone(models.Model):
	distributor = models.OneToOneField(Profile, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=30, blank=True, null=True)
	scope = models.CharField(max_length=10, blank=True, null=True)

	def __str__(self):
		return self.name

	def get_name(self):
		return self.name

	def get_scope(self):
		return self.scope