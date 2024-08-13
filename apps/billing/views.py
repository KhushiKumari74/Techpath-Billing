from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Consigner, Consignee, Vehicle, Invoice
import json
import random
from datetime import datetime
from django.http import HttpResponse
from django.views.generic import View
from .process import render_to_pdf 
from django.contrib.auth.models import User
from .utils import *
from apps.whitelable.utils import get_user_data

#Creating a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        invoice = request.GET.get('invoice')
        getInvoice = get_invoice(invoice, request)
        data=get_user_data(request)
        context={
            "invoice":getInvoice
        }
        context.update(data)
        pdf = render_to_pdf('web/invoice.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = getInvoice["invoice_number"]+".pdf"
            content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")

@login_required(login_url='login')
def add_invoice(request):
    vehicles = Vehicle.objects.filter(user=request.user).order_by('-id')
    return render(request, 'web/ntcform.html', {'vh':vehicles})

@login_required(login_url='login')
def invoice_filter(request):
    return render(request, 'web/Invoice-filter.html')

@login_required(login_url='login')
def driver_ladger(request):
    vehicles = Vehicle.objects.filter(user=request.user).order_by('-id')
    return render(request, 'web/driverladger.html', {'vehicles': vehicles})

@login_required(login_url='login')
def adddriver_ladger(request):
    if request.method == 'POST':
        user = request.user
        truck_no = request.POST.get('truck_no', None)
        driver_name = request.POST.get('driver_name', None)
        driver_address = request.POST.get('driver_address', None)
        contact_no = request.POST.get('contact_no', None)
        engine_no = request.POST.get('engine_no', None)
        chasis_no = request.POST.get('chasis_no', None)
        dl_no = request.POST.get('dl_no', None)
        owner_name = request.POST.get('vehicle_owner_name', None)
        owner_address = request.POST.get('owner_address', None)
        owner_contact = request.POST.get('owner_contact', None)
        owner_pan = request.POST.get('owner_pan', None)
        
        # You might want to add some validation before saving
        Vehicle.objects.create(
            user=user,
            truck_no=truck_no,
            driver_name=driver_name,
            driver_address=driver_address,
            contact_no=contact_no,
            engine_no=engine_no,
            chasis_no=chasis_no,
            dl_no=dl_no,
            owner_name=owner_name,
            owner_address=owner_address,
            owner_contact=owner_contact,
            owner_pan=owner_pan,
        )
        return redirect('create_driver')
    if request.method=="GET":
        return render(request, 'web/add-driver.html')

@login_required(login_url='login')
def updatedriver_ladger(request):
    if request.method == 'POST':
        vehicle = Vehicle.objects.update_or_create(
            id=request.GET.get('id'),
            defaults={
                'truck_no': request.POST.get('truck_no', None),
                'driver_name': request.POST.get('driver_name', None),
                'driver_address': request.POST.get('driver_address', None),
                'contact_no': request.POST.get('contact_no', None),
                'engine_no': request.POST.get('engine_no', None),
                'chasis_no': request.POST.get('chasis_no', None),
                'dl_no': request.POST.get('dl_no', None),
                'owner_name': request.POST.get('vehicle_owner_name', None),
                'owner_address': request.POST.get('owner_address', None),
                'owner_contact': request.POST.get('owner_contact', None),
                'owner_pan': request.POST.get('owner_pan', None),
            }
        )

        return redirect('create_driver')  # Assuming you have a view to list vehicles
    if request.method=="GET":
        id = request.GET.get('id')
        vehicles = Vehicle.objects.filter(user=request.user, id= id).first()
        return render(request, 'web/update-driverladger.html',{"vh":vehicles})

@login_required(login_url='login')
def viewdriver_details(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        vehicles = Vehicle.objects.filter(user=request.user, id= id).first()
        return render(request, 'web/viewdriver-details.html',{"vh":vehicles})

@login_required(login_url='login')
def ntc_invoice(request):
    invoice = request.GET.get('invoice')
    getInvoice = get_invoice(invoice, request)
    context={
        "invoice":getInvoice
    }
    return render(request, 'web/ntcinvoice.html', context)

@csrf_exempt
@login_required(login_url='login')
def add_invoice_with_details(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user = User.objects.filter(id=request.user.id).first()
            # Create Consigner
            consigner_data = data.get('consigner')
            consigner = Consigner(
                user = user,
                name=consigner_data['name'],
                gst_no=consigner_data['gst_no'],
                state_code=consigner_data['state_code'],
                address=consigner_data['address'],
            )
            consigner.save()

            # Create Consignee
            consignee_data = data.get('consignee')
            consignee = Consignee(
                user = user,
                name=consignee_data['name'],
                gst_no=consignee_data['gst_no'],
                state_code=consignee_data['state_code'],
                address=consignee_data['address'],
            )
            consignee.save()

            # Create Vehicle
            vehicle_data = data.get('vehicle')
            vehicle = Vehicle.objects.filter(user=request.user, id= int(vehicle_data['id'])).first()
            print(vehicle)
            # Create Invoice
            invoice_data = data.get('invoice')
            try:
                invoice = Invoice(
                    user = user,
                    invoice_number = "nct-"+ invoice_data['nature_of_goods'][:3] + "-" + str(random.randint(1,999999)),
                    from_field=invoice_data['from_field'],
                    to_field=invoice_data['to_field'],
                    consigner=consigner,
                    consignee=consignee,
                    vehicle = vehicle,
                    nature_of_goods=invoice_data['nature_of_goods'],
                    weight=invoice_data['weight'],
                    freight_rate=invoice_data['freight_rate'],
                    freight_total=invoice_data['freight_total'],
                    toll_tax=invoice_data['toll_tax'],
                    gr_sr_charges=invoice_data['gr_sr_charges'],
                    fooding=invoice_data['fooding'],
                    kata=invoice_data['kata'],
                    gst=invoice_data['gst'],
                    advance=invoice_data['advance'],
                    payable_amt=invoice_data['payable_amt'],
                    e_way_bill_no=invoice_data['e_way_bill_no'],
                    date = datetime.strptime(invoice_data.get('date'), "%d-%m-%Y").strftime("%Y-%m-%d")
                )
                invoice.save()
            except Exception as e:
                print(e)

            return JsonResponse({'status': 'success', 'invoice_number': invoice.invoice_number})
        
        except Exception as e:
            print(e)
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Only POST requests are allowed'})

@login_required(login_url='login')
def get_all_invoices(request):
    if request.method == 'GET':
        invoice_list = all_invoices(request.user)
        
        # print(invoice_list)
        context={
            "invoice_list":invoice_list
        }
        return render(request, 'web/Invoice-filter.html', context)

@login_required(login_url='login')
def ntc_invoice_update(request):
    if request.method == 'GET':
        invoice = request.GET.get('invoice')
        getInvoice = get_invoice(invoice, request)
        vehicles = Vehicle.objects.filter(user=request.user).order_by('-id')

        context={
            "invoice":getInvoice,
            "vh":vehicles
        }
        return render(request, 'web/ntcform-update.html', context)
    
@require_http_methods(["POST"])
@csrf_exempt
@login_required(login_url='login')
def update_invoice_with_details(request):
    # try:
    if 1==1:
        data = json.loads(request.body)
        invoice_id = data.get('invoice')['id']
        invoice_number = data.get('invoice')['invoice_number']

        # Check if the invoice exists
        invoice = Invoice.objects.filter(id=invoice_id).first()
        print(invoice)
        if not invoice:
            return JsonResponse({'status': 'error', 'message': 'Invoice not found.'})

        # Update Consigner
        consigner_data = data.get('consigner')
        consigner, _ = Consigner.objects.update_or_create(
            id=invoice.consigner.id,
            defaults={
                'name': consigner_data['name'],
                'gst_no': consigner_data['gst_no'],
                'state_code': consigner_data['state_code'],
                'address': consigner_data['address'],
            }
        )

        # Update Consignee
        consignee_data = data.get('consignee')
        consignee, _ = Consignee.objects.update_or_create(
            id=invoice.consignee.id,
            defaults={
                'name': consignee_data['name'],
                'gst_no': consignee_data['gst_no'],
                'state_code': consignee_data['state_code'],
                'address': consignee_data['address'],
            }
        )

        # Update Vehicle
        vehicle_data = data.get('vehicle')
        print(vehicle_data)
        vehicle = Vehicle.objects.filter(user=request.user, id= int(vehicle_data['id'])).first()

        # Update Invoice
        invoice_data = data.get('invoice')
        invoice.invoice_number = invoice_number  # Optionally modify if necessary
        invoice.from_field = invoice_data['from_field']
        invoice.to_field = invoice_data['to_field']
        invoice.consigner = consigner
        invoice.consignee = consignee
        invoice.vehicle = vehicle
        invoice.nature_of_goods = invoice_data['nature_of_goods']
        invoice.weight = invoice_data['weight']
        invoice.freight_rate = invoice_data['freight_rate']
        invoice.freight_total = invoice_data['freight_total']
        invoice.toll_tax = invoice_data['toll_tax']
        invoice.gr_sr_charges = invoice_data['gr_sr_charges']
        invoice.fooding = invoice_data['fooding']
        invoice.kata = invoice_data['kata']
        invoice.gst = invoice_data['gst']
        invoice.advance = invoice_data['advance']
        invoice.payable_amt = invoice_data['payable_amt']
        invoice.e_way_bill_no = invoice_data['e_way_bill_no']
        invoice.date = datetime.strptime(invoice_data.get('date'), "%d-%m-%Y").strftime("%Y-%m-%d")
        invoice.save()

        return JsonResponse({'status': 'success', 'message': 'Invoice updated successfully', 'invoice_number': invoice.invoice_number})
    
    # except Exception as e:
    #     print(e)
    #     return JsonResponse({'status': 'error', 'message': str(e)})