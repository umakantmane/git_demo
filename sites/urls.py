from django.conf.urls import url
from sites import views

urlpatterns = [

    url(r'^signup$', views.signUp, name='signup'),
    url(r'^signin$', views.signIn, name='signin'),
    url(r'^dashboard$', views.dashBoard, name='dashboard'),
    url(r'^logout$', views.logOut, name='logout'),

    url(r'^static_example$', views.staticExample, name='static_example'),
]


