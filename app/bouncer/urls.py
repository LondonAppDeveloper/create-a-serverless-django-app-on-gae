"""
URL Mappings for bouncer.
"""
from django.urls import path

from bouncer import views


app_name = 'bouncer'


urlpatterns = [
    path('<str:name>/', views.redirect, name='redirect'),
    path('', views.landing, name='landing'),
]
