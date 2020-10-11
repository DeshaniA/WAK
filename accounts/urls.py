from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('contracts/', views.contracts, name="contracts"),
    path('customer/<str:pk_test>/', views.customer, name="customer"),

    path('create_contract/<str:pk>/', views.createContract, name="create_contract"),
    path('update_contract/<str:pk>/', views.updateContract, name="update_contract"),
    path('delete_contract/<str:pk>/', views.deleteContract, name="delete_contract"),

]