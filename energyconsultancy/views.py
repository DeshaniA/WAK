from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
import stripe

stripe.api_key = "sk_test_51HP81IGVpbBrVqWB53exgfmStGw4Zs46SQs66J1UEP0DBXWfkIDn8ixZ9UX8maYH1bzQXJteibey460SlNuaL6e7002DJpYAnF"

def home_page(request):
    return render(request, "home.html", {"title": "Energy Consultancy"})


def domestic_page(request):
    return render(request, "domestic.html", {"title": "Energy Consultancy"})


def business_page(request):
    return render(request, "business.html", {"title": "Energy Consultancy"})


def office_page(request):
    return render(request, "office.html", {"title": "Energy Consultancy"})


def payment_page(request):
    return render(request, "payment.html")


def charge(request):

    if request.method == 'POST':
	    print('Data:', request.POST)


    amount = int(request.POST['amount'])

    customer = stripe.Customer.create(

        email = request.POST['email'],
        name=request.POST['nickname'],
        source=request.POST['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer,
        amount=amount*100,
        currency='lkr',
        description="Payment for energy consultancy 1st investigation"
    )

    return redirect(reverse('success', args=[amount]))


def firstpaid_page(request, args):
    amount = args
    return render(request, "firstPaid.html", {"amount": amount})


def form_page(request):
    return render(request, "form.html")

