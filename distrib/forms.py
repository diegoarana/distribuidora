from django import forms
from .models.sale_visit import Sale_visit

class SaleVisitForm(forms.ModelForm):
	class Meta:
		model=Sale_visit
		fields=['succes','comment']

	#change the label in forms
	def __init__(self, *args, **kwargs):
		super(SaleVisitForm, self).__init__(*args, **kwargs)
		self.fields['comment'].label = "Comentarios"
		