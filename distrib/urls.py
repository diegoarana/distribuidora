"""playa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
		https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
		1. Add an import:  from my_app import views
		2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
		1. Add an import:  from other_app.views import Home
		2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
		1. Import the include() function: from django.conf.urls import url, include
		2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from . import views

urlpatterns = [
		url(r'^$', views.homepage, name='homepage'),
		url(r'^inicio/$', views.inicio_distribuidor, name='inicio_distribuidor'),
		url(r'^client/$', views.client),
		url(r'^client/(?P<id>[0-9]+)/$', views.client_detail, name='client_detail'),
		#url(r'^products/(?P<pk>[0-9]+)$', views.product_detail),

]
