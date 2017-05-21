from django.contrib import admin

from import_export import resources
from .models import tbl_profiles, tbl_due_listing
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class DebtResource(resources.ModelResource):

    class Meta:
        model = tbl_profiles


        #exclude = ('')
        fields = ('id','date','principal_amt','intrest_rate', 'monthly_payment', 'customer',)

class DebtAdmin(ImportExportModelAdmin):
    resource_class = DebtResource

    list_display =  ('date','principal_amt','intrest_rate', 'monthly_payment', 'customer')
    #search_fields = ['customer_id', 'phone_number' ]
    #list_filter = ['original_amt']

class CustomerResource(resources.ModelResource):

    class Meta:
        model = tbl_due_listing


        #exclude = ('')
        fields = ('id','date_joined','customer_id','first_name', 'last_name', 'phone_number',)

class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource

    list_display =  ('date_joined','customer_id','first_name', 'last_name', 'phone_number')
    search_fields = ['customer_id', 'phone_number' ]
    #list_filter = ['original_amt']
    

    
admin.site.register(tbl_profiles, DebtAdmin)
admin.site.register(tbl_due_listing, CustomerAdmin)



