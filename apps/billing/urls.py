from django.urls import path
from .views import invoice_filter,add_invoice, driver_ladger,adddriver_ladger,updatedriver_ladger,viewdriver_details, add_invoice_with_details, GeneratePdf, ntc_invoice, get_all_invoices, ntc_invoice_update, update_invoice_with_details

urlpatterns = [
    path('', get_all_invoices, name='invoice_filter'),
    path('create-invoice/', add_invoice, name='create_invoice'),
    # path('invoice/', invoice, name='invoice'),
    path('add/invoice/', add_invoice_with_details, name='add_invoice_with_details'),
    path('update/invoice/', update_invoice_with_details, name='update_invoice_with_details'),
    path('pdf-invoice/', GeneratePdf.as_view()),
    path('view-invoice/', ntc_invoice, name="view_invoice"),
    path('driver-ladger/', driver_ladger, name="create_driver"),
    path('adddriver-ladger/', adddriver_ladger, name="add_driver"),
    path('updatedriver-ladger/',updatedriver_ladger, name="update_driver"),
    path('viewdriver-details/',viewdriver_details, name="view-driverdetails"),
    path('update-invoice/', ntc_invoice_update, name="view_invoice_update")
]
