from django.contrib import admin

# Register your models here.
from .models import cusStatus
from .models import cusDetails
from .models import paymentDetails

class CusstatusAdmin(admin.ModelAdmin):
    list_display = ('cusName', 'projDetails', 'location', 'totPrice')


class CusdetailsAdmin(admin.ModelAdmin):
    list_display = ('cusName', 'projDetails', 'location', 'totPrice', 'stageOnePrice', 'stageTwoPrice', 'stageThreePrice')

class CuspaymentdetailsAdmin(admin.ModelAdmin):
    list_display = ('fName', 'lName', 'email', 'phone', 'address', 'address2', 'city', 'AccNo', 'tariff',
                    'unitMon1', 'unitMon2', 'unitMon3', 'supMon1', 'supMon2', 'supMon3')


admin.site.register(cusStatus, CusstatusAdmin)
admin.site.register(cusDetails, CusdetailsAdmin)
admin.site.register(paymentDetails,CuspaymentdetailsAdmin)

