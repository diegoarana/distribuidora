from django import forms
from .models.sale_visit import Sale_visit
from .models.sale_item import Sale_item
from .models.payment import Payment

class SaleVisitForm(forms.ModelForm):
	class Meta:
		model=Sale_visit
		fields=['succes','comment']

	#change the label in forms
	def __init__(self, *args, **kwargs):
		super(SaleVisitForm, self).__init__(*args, **kwargs)
		self.fields['comment'].label = "Comentarios"

class SaleItemForm(forms.ModelForm):
	class Meta:
		model=Sale_item
		fields=['item', 'product', 'quantity']
		

class PaymentForm(forms.ModelForm):
	class Meta:
		model=Payment
		fields=['amount']

	def __init__(self, *args, **kwargs):
		super(PaymentForm, self).__init__(*args, **kwargs)
		self.fields['amount'].label = "Monto"
