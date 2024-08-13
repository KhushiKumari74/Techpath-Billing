from django.contrib import admin
from .models import Profile, Company, MobileNumber, User

class MobileNumberInline(admin.TabularInline):
    model = MobileNumber
    extra = 1

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email')
    inlines = [MobileNumberInline]

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'reg_no', 'state_code', 'service_regd', 'bank_name', 'account_number', 'ifsc', 'address')
    list_filter = ('name','state_code', 'service_regd', 'bank_name')