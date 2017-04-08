from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator
from .profile import Profile
from .debt import Debt

class Client(models.Model):
	administrator = models.ForeignKey(Profile, on_delete=models.CASCADE)
	name = models.CharField(max_length=30, blank=True, null=True)
	surname = models.CharField(max_length=30, blank=True, null=True)
	dni = models.PositiveIntegerField(help_text="(Solamente dígitos)", validators=[MaxValueValidator(99999999)], blank = True, null = True)
	phone = models.PositiveIntegerField(help_text="(Solamente dígitos)", validators=[MaxValueValidator(999999999999999)], blank = True, null = True)
	address = models.CharField(blank=True, null=True, max_length=30)
	debt = models.OneToOneField(Debt, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.name

	def get_borrowed(self):
		try:
			b = self.borrowed_set.all()
		except:
			pass
		return b

	def get_name(self):
		return self.name

	def get_dni(self):
		return self.dni

	def get_phone(self):
		return self.phone

	def get_address(self):
		return self.address
