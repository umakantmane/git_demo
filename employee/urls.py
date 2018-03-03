from django.conf.urls import url
from employee import views

urlpatterns = [

    url(r'^emp_hello$', views.emp_example, name="emp_hello"),

]