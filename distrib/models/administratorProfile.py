from __future__ import unicode_literals
from django.db import models

class AdministratorProfile(models.Model):
	sector = models.CharField(max_length=30, blank=True, null=True)

	def get_sector(self):
		return self.sector

	class Meta:
		abstract = True