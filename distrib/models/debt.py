from django.db import models

# Clase deuda, con fecha desde que pago el total de la deduda y fecha de la actual
# Por ahora solamente hice que la deuda sea un campo de cliente
class Debt(models.Model):
	amount = models.DecimalField(max_digits = 8, decimal_places = 2, blank = True, null = True)
	date_from_zero = models.DateTimeField(auto_now_add = True)
	date_from_act = models.DateTimeField(auto_now_add=True)