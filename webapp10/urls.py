"""webapp10 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcomes),
    path('load_form', views.load_form),
    path('add', views.add),
    path('load_forms', views.load_forms),
    path('adds', views.adds),
    path('loaded_form', views.loaded_form),
    path('added', views.added),
    path('loaded_forms', views.loaded_forms),
    path('adding', views.adding),
    path('show', views.show),
    path('shows', views.shows),
    path('showss', views.showss),
    path('showes', views.showes),
    path('edit/<int:id>', views.edit),
    path('edits/<int:id>', views.edits),
    path('edited/<int:id>', views.edited),
    path('editing/<int:id>', views.editing),
    path('update/<int:id>', views.update),
    path('updats/<int:id>', views.updats),
    path('updates/<int:id>', views.updates),
    path('updated/<int:id>', views.updated),
    path('delete/<int:id>', views.delete),
    path('deletes/<int:id>', views.deletes),
    path('deleted/<int:id>', views.deleted),
    path('deleting/<int:id>', views.deleting),
    path('search', views.search),
]
