from django import forms
from .models.sale_visit import Sale_visit

class SaleVisitForm(forms.ModelForm):
	class Meta:
		model=Sale_visit
		fields=['succes','product','total_amount','comment']