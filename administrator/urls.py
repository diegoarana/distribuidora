from django.conf.urls import url, include
from . import views

urlpatterns = [
		url(r'^index_admin/$', views.index_admin, name='inicio_administrador'),

]