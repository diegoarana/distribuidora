from django import forms
from distrib.models.client import Client
from distrib.models.profile import Profile
from distrib.models.product import Product
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)

class ClientForm(forms.ModelForm):
	class Meta:
		model=Client
		fields=['name', 'surname', 'dni', 'address', 'phone']

	#change the label in forms
	def __init__(self, *args, **kwargs):
		super(ClientForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = "Nombre"
		self.fields['surname'].label = "Apellido"
		self.fields['dni'].label = "DNI"
		self.fields['address'].label = "Dirección"
		self.fields['phone'].label = "Telefóno"        

class ProfileForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['name', 'surname', 'address', 'phone']

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['address'].label = "Dirección - Calle"
		self.fields['phone'].label = "Teléfono"
		self.fields['name'].label = "Nombre"
		self.fields['surname'].label = "Apellido"

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['name', 'price', 'description']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nombre"
        self.fields['price'].label = "Precio"
        self.fields['description'].label = "Descripción"

class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': ("The two password fields didn't match."),
    }
    password1 = forms.CharField(
        label=("Contraseña"),
        strip=False,
        widget=forms.PasswordInput,
        help_text=("Mínimo 8 caracteres"),
    )
    password2 = forms.CharField(
        label=("Reescribir contraseña"),
        widget=forms.PasswordInput,
        strip=False,
        help_text=("Ingrese nuevamente la contraseña para verificar"),
    )

    class Meta:
        model = User
        fields = ['username']
        #field_classes = {'username': UsernameField}

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Nombre de usuario"
        self.fields['username'].help_text = "Letras, dígitos y @/./+/-/_ solamente"
        self.fields[self._meta.model.USERNAME_FIELD].widget.attrs.update({'autofocus': ''})

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas NO son iguales")
        self.instance.username = self.cleaned_data.get('username')
        password_validation.validate_password(self.cleaned_data.get('password2'), self.instance)
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user