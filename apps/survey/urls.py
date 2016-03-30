print "survey urls"
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process', views.process, name='process'),
    url(r'^result$', views.result, name='result'),
]
