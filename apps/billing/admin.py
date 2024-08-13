from django.contrib import admin
from .models import Consigner, Consignee, Vehicle, Invoice

@admin.register(Consigner)
class ConsignerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'gst_no', 'state_code', 'address')
    search_fields = ('user', 'name', 'gst_no', 'state_code')

@admin.register(Consignee)
class ConsigneeAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'gst_no', 'state_code', 'address')
    search_fields = ('user', 'name', 'gst_no', 'state_code')

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('user','truck_no', 'driver_name', 'contact_no', 'owner_name')
    search_fields = ('user','truck_no', 'driver_name', 'owner_name')

    fieldsets = (
        ('Select User', {
            'fields': ('user',)
        }),
        ('Vehicle Information', {
            'fields': ('truck_no', 'driver_name', 'driver_address', 'contact_no', 'engine_no', 'chasis_no', 'dl_no')
        }),
        ('Owner Information', {
            'fields': ('owner_name', 'owner_address', 'owner_contact', 'owner_pan')
        }),
    )
@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('user','invoice_number', 'from_field', 'to_field', 'consigner', 'consignee', 'vehicle', 'nature_of_goods', 'weight', 'freight_total', 'payable_amt', 'date')
    search_fields = ('user','invoice_number', 'from_field', 'to_field', 'consigner__name', 'consignee__name', 'nature_of_goods')

    fieldsets = (
        ('Invoice Information', {
            'fields': ('invoice_number', 'date','user')
        }),
        ('Location Information', {
            'fields': ('from_field', 'to_field')
        }),
        ('Consigner and Consignee', {
            'fields': ('consigner', 'consignee')
        }),
        ('Goods Information', {
            'fields': ('nature_of_goods', 'weight')
        }),
        ('Freight Details', {
            'fields': ('freight_rate', 'freight_total', 'toll_tax', 'gr_sr_charges')
        }),
        ('Expenses', {
            'fields': ('fooding', 'kata', 'gst', 'advance', 'payable_amt')
        }),
        ('E-Way Bill', {
            'fields': ('e_way_bill_no',)
        }),
        ('Truck and  Driver', {
            'fields': ('vehicle',)
        }),
    )

    readonly_fields = ('payable_amt',)