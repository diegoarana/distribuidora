from __future__ import unicode_literals
from django.db import models
from .profile import Profile

class Visit(models.Model):
	distributor = models.ForeignKey(Profile, on_delete=models.CASCADE)
	succes = models.BooleanField("Hay gente en el domicilio", default=False)
	date = models.DateTimeField(auto_now_add=True)
	comment = models.TextField(blank=True, max_length=100)

	def __str__(self):
		return self.distributor.name

	def get_succes(self):
		self.succes

	def get_date(self):
		self.date

	def get_comment(self):
		self.comment