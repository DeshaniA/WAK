from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
# Create your views here.
from .models import *
from .forms import ContractForm


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


def createContract(request, pk):
    ContractFormSet=inlineformset_factory(Customer, Contract, fields=('service', 'status'))
    customer=Customer.objects.get(id=pk)
    formset=ContractFormSet(instance=customer)
    #form = ContractForm(initial={'customer':customer})
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        #form = ContractForm(request.POST)
        formset = ContractFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset':formset}
    return render(request, 'accounts/contract_form.html', context)


def updateContract(request, pk):

    contract = Contract.objects.get(id=pk)
    form = ContractForm(instance=contract)

    if request.method == 'POST':
        form = ContractForm(request.POST, instance=contract)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/contract_form.html', context)


def deleteContract(request, pk):
    contract = Contract.objects.get(id=pk)
    if request.method == "POST":
        contract.delete()
        return redirect('/')

    context = {'item':contract}
    return render(request, 'accounts/delete.html', context)
