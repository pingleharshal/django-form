from django.urls import include
from django.contrib import admin
from django.urls import path
from .views import home_view

#from myApp.views import hello_geek

urlpatterns = [
    path('', home_view),

]