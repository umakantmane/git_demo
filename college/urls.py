from django.conf.urls import url
from college import views

urlpatterns = [

    url(r'^hello$', views.hello, name="hello"),
    url(r'^hello_django$', views.django_layout, name="hello2"),
    url(r'^form_example$', views.form_example, name="form_example"),
    url(r'^core_html$', views.core_html, name="form_example"),
]