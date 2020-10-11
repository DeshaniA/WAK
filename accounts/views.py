from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *


def home(request):
    contracts = Contract.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_contracts = contracts.count()
    finished = contracts.filter(status='Finished').count()
    pending = contracts.filter(status='Pending').count()

    context = {'contracts': contracts, 'customers': customers,
               'total_contracts': total_contracts, 'finished': finished,
               'pending': pending}

    return render(request, 'accounts/dashboard.html', context)


def contracts(request):
    services = Service.objects.all()

    return render(request, 'accounts/contracts.html', {'services': services})


def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    contracts=customer.contract_set.all()
    contract_count=contracts.count()

    context = {'customer': customer, 'contracts': contracts,'contract_count':contract_count}
    return render(request, 'accounts/customer.html', context)
