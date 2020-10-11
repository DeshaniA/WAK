from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('contracts/', views.contracts, name="contracts"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),
]