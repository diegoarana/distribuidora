from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator
from .profile import Profile
from .client import Client
from .borrowed import Borrowed

class Sale_visit(models.Model):
	distributor = models.ForeignKey(Profile, on_delete=models.CASCADE)
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	succes = models.BooleanField("Hay gente en el domicilio?", default=True)
	date = models.DateTimeField(auto_now_add=True)
	total_amount = models.PositiveSmallIntegerField(validators=[MaxValueValidator(999)], blank = True, null = True)
	comment = models.TextField(blank=True, max_length=100)

	def __str__(self):
		return '%s - %s' % (self.distributor.name, self.client)

	class Meta:
		ordering = ['-date']

	def get_date(self):
		return self.date

	def calculate_total(self):
		total = 0
		try:
			items = self.sale.all()
		except:
			pass

		if items:
			for i in items:
				aux = 0
				aux = i.quantity * i.product.price
				total +=  aux

		return total
		
	def borrow_products(self):
		products = self.sale.all()
		for p in products:
			cant = p.quantity
			for i in range(cant):
				borrow = Borrowed()
				borrow.client = self.client
				borrow.product = p.product
				borrow.save()
				borrow = None
