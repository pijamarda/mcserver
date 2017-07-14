from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^logout/$', auth_views.logout,{'template_name': 'logged_out.html'} , name='logout'),
]

