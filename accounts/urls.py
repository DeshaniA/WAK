from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('contracts/', views.contracts),
    path('customer/', views.customer),
]