from django.shortcuts import render, redirect
from .models import Supplier
from .models import Product
from .models import Contract
from .models import Rating
from .forms import SupplierForm
from .forms import ProductForm
from .forms import ContractForm
from .forms import RatingForm


def welcomes(request):
    return render(request, "welcomes.html")


def load_form(request):
    form = SupplierForm
    return render(request, "insert.html", {'form': form})


def add(request):
    form = SupplierForm(request.POST)
    form.save()
    return redirect('/show')


def load_forms(request):
    form = ProductForm
    return render(request, "products.html", {'form': form})


def adds(request):
    form = ProductForm(request.POST)
    form.save()
    return redirect('/shows')

def loaded_form(request):
    form = ContractForm
    return render(request, "contracts.html", {'form': form})


def added(request):
    form = ContractForm(request.POST)
    form.save()
    return redirect('/showss')

def loaded_forms(request):
    form = RatingForm
    return render(request, "ratings.html", {'form': form})


def adding(request):
    form = RatingForm(request.POST)
    form.save()
    return redirect('/showes')


def show(request):
    supplier = Supplier.objects.all
    return render(request, 'show.html', {'supplier': supplier})


def shows(request):
    product = Product.objects.all
    return render(request, 'shows.html', {'product': product})


def showss(request):
    contract = Contract.objects.all
    return render(request, 'showss.html', {'contract': contract})


def showes(request):
    rating = Rating.objects.all
    return render(request, 'showes.html', {'rating': rating})


def edit(request, id):
    supplier = Supplier.objects.get(id=id)
    return render(request, 'edit.html', {'supplier': supplier})


def edits(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'edits.html', {'product': product})


def edited(request, id):
    contract = Contract.objects.get(id=id)
    return render(request, 'edited.html', {'contract': contract})


def editing(request, id):
    rating = Rating.objects.get(id=id)
    return render(request, 'editing.html', {'rating': rating})


def update(request, id):
    supplier = Supplier.objects.get(id=id)
    form = SupplierForm(request.POST, instance=supplier)
    form.save()
    return redirect('/show')


def updats(request, id):
    product = Product.objects.get(id=id)
    form = ProductForm(request.POST, instance=product)
    form.save()
    return redirect('/shows')

def updates(request, id):
    contract = Contract.objects.get(id=id)
    form = ContractForm(request.POST, instance=contract)
    form.save()
    return redirect('/showss')


def updated(request, id):
    rating = Rating.objects.get(id=id)
    form = RatingForm(request.POST, instance=rating)
    form.save()
    return redirect('/showes')


def delete(request, id):
    supplier = Supplier.objects.get(id=id)
    supplier.delete()
    return redirect('/show')


def deletes(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('/shows')


def deleted(request, id):
    contract = Contract.objects.get(id=id)
    contract.delete()
    return redirect('/showss')


def deleting(request, id):
    rating = Rating.objects.get(id=id)
    rating.delete()
    return redirect('/showes')


def search(request):
    given_name = request.POST['name']
    supplier = Supplier.objects.filter(ename__icontains=given_name)
    return render(request, 'show.html', {'supplier': supplier})


