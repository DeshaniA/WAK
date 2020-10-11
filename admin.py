from django.contrib import admin

# Register your models here.
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('ename_f','ename_l','econtact','egender','ehometown')

class Finance(admin.ModelAdmin):
    list_display = ()


admin.site.register(Employee, EmployeeAdmin)
