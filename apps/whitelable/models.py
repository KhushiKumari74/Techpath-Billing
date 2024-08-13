from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return "{}'s Profile".format(self.name)

class MobileNumber(models.Model):
    profile = models.ForeignKey(Profile, related_name='mobile_numbers', on_delete=models.CASCADE)
    number = models.CharField(max_length=15)

    def __str__(self):
        return self.number

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company',null=True)
    name= models.CharField(max_length=255,blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/',blank=True, null=True)
    reg_no = models.CharField(max_length=255,blank=True, null=True)
    state_code = models.CharField(max_length=10,blank=True, null=True)
    service_regd = models.CharField(max_length=255,blank=True, null=True)
    bank_name = models.CharField(max_length=255,blank=True, null=True)
    account_number = models.CharField(max_length=20,blank=True, null=True)
    ifsc = models.CharField(max_length=11,blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    billing_statement =  models.TextField(blank=True, null=True)

    def __str__(self):
        return self.reg_no
