from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'api/encender/$', views.encender, name='encender'),
    url(r'api/encenderminecraft/$', views.encender_minecraft, name='encender_minecraft'),
]