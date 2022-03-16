from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home page'),
    path('search',views.search,name='search'),
    path('new_search',views.new_search,name='new_search'),
]