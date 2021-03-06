from django.contrib import admin
from .models.profile import Profile
from .models.client import Client
from .models.product import Product
from .models.sale_item import Sale_item
from .models.sale_visit import Sale_visit
from .models.visit import Visit
from .models.zone import Zone
from .models.camion import Camion
from .models.borrowed import Borrowed

# Register your models here.

admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Sale_item)
admin.site.register(Sale_visit)
admin.site.register(Visit)
admin.site.register(Zone)
admin.site.register(Camion)
admin.site.register(Borrowed)