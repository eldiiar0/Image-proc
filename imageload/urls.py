from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'imageload'
urlpatterns = [
    path('', main, name='main'),
    path('homepage/', homepage, name='homepage'),
    path('detect/', img_detect, name='img_detect'),    
]