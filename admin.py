from django.contrib import admin

# Register your models here.
from .models import Employee
from .models import Time

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('ename_f', 'ename_l', 'econtact', 'egender', 'ehometown')

class TimeAdmin(admin.ModelAdmin):
    list_display = ('ename_f', 'ename_l', 'eIntime','eOuttime','eOtherinfo')

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Time, TimeAdmin)


