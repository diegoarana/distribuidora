from __future__ import unicode_literals
from django.db import models
from django.core.validators import MaxValueValidator
from .profile import Profile
from .debt import Debt
import collections

class Client(models.Model):
	administrator = models.ForeignKey(Profile, on_delete=models.CASCADE)
	name = models.CharField(max_length=30, blank=False, null=False,)
	surname = models.CharField(max_length=30, blank=False, null=False,)
	dni = models.PositiveIntegerField(help_text="(Solamente dígitos)", validators=[MaxValueValidator(99999999)], blank=False, null=False,)
	phone = models.PositiveIntegerField(help_text="(Solamente dígitos)", validators=[MaxValueValidator(999999999999999)], blank=False, null=False,)
	address = models.CharField(blank=False, null=False, max_length=30)
	debt = models.PositiveIntegerField(validators=[MaxValueValidator(999999)], null=False, default=0)

	class Meta:
		ordering = ['surname']

	def __str__(self):
		return self.name

	def get_borrowed(self):
		try:
			b = self.borrowed_set.all()
		except:
			pass
		return b

	# retorna diccionario(id:cantidad) con la cantidad prestda de cada producto(id)  
	def contarPrestados(self):
		listaPrestados = self.borrowed_set.all()
		listaIds=[]

		for l in listaPrestados:
			listaIds.append(l.product.name)

		dic = collections.Counter(listaIds)
		dic = dict(dic)
		return dic

	def devolver_envases(self, cantidad, nombre):
		# Eliminar la cantidad de envases de ese nombre
		# navegar entre relaciones desde cliente para obtener los envases de ese nombre
		# y luego hacer .delete() la cantidad de veces
		listaPrestados = self.borrowed_set.all()
		seleccion = listaPrestados.filter(product__name__icontains=nombre)[:cantidad]
		for s in seleccion:
			s.delete()
		return None



	def get_sales(self):
		s = self.sale_visit_set.filter(succes=True)
		return s

	def get_visits(self):
		v = self.sale_visit_set.filter(succes=False)
		return v

	def get_payments(self):
		p = self.payment_set.all()
		return p

	def get_name(self):
		return self.name

	def get_dni(self):
		return self.dni

	def get_phone(self):
		return self.phone

	def get_address(self):
		return self.address
