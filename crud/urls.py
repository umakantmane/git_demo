from django.conf.urls import url
from crud import views

urlpatterns = [

    url(r'^create$', views.create, name="create"),
    url(r'^index$', views.index, name="index"),
    url(r'^update/(?P<pk>[0-9]+)$', views.update, name="update"),
    url(r'^delete/(?P<pk>[0-9]+)$', views.delete, name="delete"),
    url(r'^view/(?P<pk>[0-9]+)$', views.view, name="view"),

    url(r'^create_customer$', views.createCustomer, name="create_customer"),
    url(r'^customer_index$', views.customerIndex, name="customer_index"),
    url(r'^update_customer/(?P<pk>[0-9]+)$', views.update_customer, name="update_customer"),
]

