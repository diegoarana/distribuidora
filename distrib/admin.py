from django.contrib import admin
from .models.profile import Profile
from .models.client import Client
from .models.product import Product
from .models.catalog import Catalog
from .models.sale import Sale
from .models.visit import Visit
from .models.zone import Zone
from .models.camion import Camion

# Register your models here.

admin.site.register(Profile)
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Catalog)
admin.site.register(Sale)
admin.site.register(Visit)
admin.site.register(Zone)
admin.site.register(Camion)