from django.db import models
from django.contrib.auth.models import User

class Consigner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consigner',null=True)
    name = models.CharField(max_length=255)
    gst_no = models.CharField(max_length=15, null=True, blank=True)
    state_code = models.CharField(max_length=255,null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name

class Consignee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='consignee',null=True)
    name = models.CharField(max_length=255)
    gst_no = models.CharField(max_length=15, null=True, blank=True)
    state_code = models.CharField(max_length=255,null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vehicle',null=True)
    truck_no = models.CharField(max_length=15, null=True, blank=True)
    driver_name = models.CharField(max_length=255)
    driver_address = models.CharField(max_length=512, null=True, blank=True)
    contact_no = models.CharField(max_length=255,null=True, blank=True)
    engine_no = models.CharField(max_length=30, null=True, blank=True)
    chasis_no = models.CharField(max_length=30, null=True, blank=True)
    dl_no = models.CharField(max_length=20, null=True, blank=True)
    owner_name = models.CharField(max_length=255, null=True, blank=True)
    owner_address = models.CharField(max_length=512, null=True, blank=True)
    owner_contact = models.CharField(max_length=15, null=True, blank=True)
    owner_pan = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.truck_no

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invoice',null=True)
    invoice_number = models.CharField(max_length=255, null=True, blank=True)
    from_field = models.CharField(max_length=255)
    to_field = models.CharField(max_length=255)
    consigner = models.ForeignKey(Consigner, on_delete=models.CASCADE)
    consignee = models.ForeignKey(Consignee, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)
    nature_of_goods = models.CharField(max_length=255)
    weight = models.CharField(max_length=255,null=True, blank=True)
    freight_rate = models.CharField(max_length=255,null=True, blank=True)
    freight_total = models.CharField(max_length=255,null=True, blank=True)
    toll_tax = models.CharField(max_length=255,null=True, blank=True)
    gr_sr_charges = models.CharField(max_length=255,null=True, blank=True)
    fooding = models.CharField(max_length=255,null=True, blank=True)
    kata = models.CharField(max_length=30, null=True, blank=True)
    gst = models.CharField(max_length=255,null=True, blank=True)
    advance = models.CharField(max_length=255,null=True, blank=True)
    payable_amt = models.CharField(max_length=255,null=True, blank=True)
    e_way_bill_no = models.CharField(max_length=30, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.invoice_number} - {self.nature_of_goods}"