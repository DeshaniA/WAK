"""energyconsultancy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from consultancy.views import (
    domestic_reg_cust_page
)
from .views import (
    home_page,
    domestic_page,
    business_page,
    office_page,
    payment_page,
    firstpaid_page,
    charge,
    form_page,
    logout_request,
    login_request,
    domreg,)

urlpatterns = [
    path('', home_page,name="home_page"),
    path('form/', form_page),
    path('consultancy/<int:post_id>/', domestic_reg_cust_page),
    path('firstPaid/<str:args>/', firstpaid_page, name="success"),
    path('payment/', payment_page, name="payment"),
    path('charge/', charge, name="charge"),
    path('office/', office_page),
    path('business/', business_page),
    path('domestic/', domestic_page),
    path('admin/', admin.site.urls),
    path("logout/", logout_request, name="logout"),
    path("login/", login_request, name="login"),
    path("domreg/",domreg,name="dom_reg_page")
]
