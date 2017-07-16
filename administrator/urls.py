from django.conf.urls import url, include
from . import views

urlpatterns = [
		url(r'^index_admin/', include([
			url(r'^$', views.buscar_cliente, name='inicio_administrador'),
			url(r'^sales$', views.sales, name='sales'),
			url(r'^sale_detail/(?P<id>[0-9]+)/$', views.sale_detail, name='sale_detail'),
			url(r'^visits$', views.visits, name='visits'),
			url(r'^distrib$', views.distrib_list, name='distrib_list'),
			url(r'^distrib/new$', views.new_distrib, name='new_distrib'),
			url(r'^distrib/edit/(?P<id>[0-9]+)$', views.distrib_edit, name='distrib_edit'),
			url(r'^distrib/chagePass/(?P<id>[0-9]+)$', views.distribChangePass, name='distribChangePass'),
			url(r'^administradores$', views.admin_list, name='admin_list'),
			url(r'^administradores/new$', views.new_admin, name='new_admin'),
			url(r'^administradores/edit/(?P<id>[0-9]+)$', views.admin_edit, name='admin_edit'),
			url(r'^administradores/chagePass/(?P<id>[0-9]+)$', views.adminChangePass, name='adminChangePass'),
			url(r'^products$', views.products, name='products'),
			url(r'^products/new$', views.new_product, name='new_product'),
			url(r'^products/edit/(?P<id>[0-9]+)/$', views.product_edit, name='product_edit'),
			url(r'^products/delete/(?P<id>[0-9]+)/$', views.product_delete, name='product_delete'),
			url(r'^client/new$', views.new_client, name='new_client'),
			url(r'^client/(?P<id>[0-9]+)/$', views.client_detail, name='client_detail_a'),
			url(r'^client/(?P<id>[0-9]+)/sales$', views.client_sales, name='client_sales'),
			url(r'^client/(?P<id>[0-9]+)/visits$', views.client_visits, name='client_visits'),
			url(r'^client/(?P<id>[0-9]+)/borrowed$', views.client_borrowed, name='client_borrowed'),
			url(r'^client/(?P<id>[0-9]+)/payments$', views.client_payments, name='client_payments'),
			url(r'^client/delete/(?P<id>[0-9]+)/$', views.client_delete, name='client_delete'),

			]))
		

]