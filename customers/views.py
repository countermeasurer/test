from django.shortcuts import render
from .models import Customer


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/customer_list.html', {'customers': customers})

def customer_detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    return render(request, 'customers/customer_detail.html', {'customer': customer})