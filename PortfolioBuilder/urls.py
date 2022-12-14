from urllib import request

from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views
from django.urls import path


urlpatterns = [

    path('index', views.Index.as_view(), name='index'),
    path('login', views.Login.as_view(), name='login'),
    path('register', views.register.as_view, name='register'),

]
