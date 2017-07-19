from django.db import models
from .client import Client
from .profile import Profile
from django.core.validators import MaxValueValidator

class Payment(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	distributor = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
	amount = models.PositiveIntegerField(validators=[MaxValueValidator(999999)], null=False, default=0)
	date = models.DateTimeField(auto_now_add = True)