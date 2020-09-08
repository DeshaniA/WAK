from django.contrib import admin

# Register your models here.
from .models import cusStatus
from .models import cusDetails


class CusstatusAdmin(admin.ModelAdmin):
    list_display = ('cusName', 'projDetails', 'location', 'totPrice')


class CusdetailsAdmin(admin.ModelAdmin):
    list_display = ('cusName', 'projDetails', 'location', 'totPrice', 'stageOnePrice', 'stageTwoPrice', 'stageThreePrice')


admin.site.register(cusStatus, CusstatusAdmin)
admin.site.register(cusDetails, CusdetailsAdmin)

