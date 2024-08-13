from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from .models import Consigner, Consignee, Vehicle, Invoice

def all_invoices(user):
    # invoices = Invoice.objects.all()
    invoices = Invoice.objects.filter(user=user).all()
    invoice_list = []

    for invoice in invoices:
        print(invoice.vehicle.truck_no)
        invoice_data = {
            "invoice_number": invoice.invoice_number,
            "id": invoice.id,
            "from_field": invoice.from_field,
            "to_field": invoice.to_field,
            "date": invoice.date,
            "consigner": {
                "name": invoice.consigner.name,
                "gst_no": invoice.consigner.gst_no,
                "state_code": invoice.consigner.state_code,
                "address": invoice.consigner.address,
            },
            "consignee": {
                "name": invoice.consignee.name,
                "gst_no": invoice.consignee.gst_no,
                "state_code": invoice.consignee.state_code,
                "address": invoice.consignee.address,
            },
            "vehicle": {
            "truck_no": invoice.vehicle.truck_no,
            "driver_name": invoice.vehicle.driver_name,
            "driver_address": invoice.vehicle.driver_address,
            "contact_no": invoice.vehicle.contact_no,
            "owner_name": invoice.vehicle.owner_name,
            "owner_address": invoice.vehicle.owner_address,
            "owner_contact": invoice.vehicle.owner_contact,
            "owner_pan": invoice.vehicle.owner_pan,
            "dl_no": invoice.vehicle.dl_no,
            "engine_no":invoice.vehicle.engine_no,
            "chasis_no":invoice.vehicle.chasis_no,
            # Here, you should include other fields of the 'vehicle' that are relevant.
            },
           
            "nature_of_goods": invoice.nature_of_goods,
            "weight": invoice.weight,
            "freight_rate": invoice.freight_rate,
            "freight_total":invoice.freight_total,
            "toll_tax": invoice.toll_tax,
            "gr_sr_charges": invoice.gr_sr_charges,
            "fooding": invoice.fooding,
            "kata": invoice.kata,
            "gst": invoice.gst,
            "advance": invoice.advance,
            "payable_amt": invoice.payable_amt,
            "e_way_bill_no": invoice.e_way_bill_no,
            "date": invoice.date,
            # Include other fields of the invoice that are relevant here.
        }

        invoice_list.append(invoice_data)

    return invoice_list

def get_invoice(invoice_id, request):
    invoice = Invoice.objects.filter(id=invoice_id, user=request.user).first()
    invoice_data = {
        "invoice_number": invoice.invoice_number,
        "id": invoice.id,
        "from_field": invoice.from_field,
        "to_field": invoice.to_field,
        "date": invoice.date,
        "consigner": {
            "name": invoice.consigner.name,
            "gst_no": invoice.consigner.gst_no,
            "state_code": invoice.consigner.state_code,
            "address": invoice.consigner.address,
        },
        "consignee": {
            "name": invoice.consignee.name,
            "gst_no": invoice.consignee.gst_no,
            "state_code": invoice.consignee.state_code,
            "address": invoice.consignee.address,
        },
        "vehicle": {
            "id":invoice.vehicle.id,
            "truck_no": invoice.vehicle.truck_no,
            "driver_name": invoice.vehicle.driver_name,
            "driver_address": invoice.vehicle.driver_address,
            "contact_no": invoice.vehicle.contact_no,
            "owner_name": invoice.vehicle.owner_name,
            "owner_address": invoice.vehicle.owner_address,
            "owner_contact": invoice.vehicle.owner_contact,
            "owner_pan": invoice.vehicle.owner_pan,
            "dl_no": invoice.vehicle.dl_no,
            "engine_no":invoice.vehicle.engine_no,
            "chasis_no":invoice.vehicle.chasis_no,
            # Here, you should include other fields of the 'vehicle' that are relevant.
        },
        "nature_of_goods": invoice.nature_of_goods,
        "weight": invoice.weight,
        "freight_rate": invoice.freight_rate,
        "freight_total":invoice.freight_total,
        "toll_tax": invoice.toll_tax,
        "gr_sr_charges": invoice.gr_sr_charges,
        "fooding": invoice.fooding,
        "kata": invoice.kata,
        "gst": invoice.gst,
        "advance": invoice.advance,
        "payable_amt": invoice.payable_amt,
        "e_way_bill_no": invoice.e_way_bill_no,
        "date": invoice.date,

        # Include other fields of the invoice that are relevant here.
    }
    return invoice_data

