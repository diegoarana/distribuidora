from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^bloque/buscar_cliente/$', views.bloque_buscar_cliente, name='bloque_buscar_cliente'),
]