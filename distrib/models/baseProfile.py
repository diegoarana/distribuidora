from __future__ import unicode_literals
from django.db import models
from django.conf import settings

class BaseProfile(models.Model):
	USER_TYPES = (
		(0, 'Administrator'),
		(1, 'Distributor'),
		)

	user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE, related_name="usuario")
	user_type = models.IntegerField(null=False, choices=USER_TYPES)
	name = models.CharField(max_length=30, blank=False, null=False)
	surname = models.CharField(max_length=30, blank=False, null=False)

	def __str__(self):
		return "{} : {}". format(self.user, self.user_type or "")

	def get_name(self):
		return self.name

	def get_surname(self):
		return self.surname
	
	class Meta:
		abstract = True
