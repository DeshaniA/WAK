from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from consultancy.models import paymentDetails
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
    fName = request.POST.get("fName",False)
    lName = request.POST.get("lName",False)
    email = request.POST.get("email",False)
    phone = request.POST.get("phone",False)
    address = request.POST.get("address",False)
    address2 = request.POST.get("address2",False)
    city = request.POST.get("city",False)
    AccNo = request.POST.get("AccNo",False)
    tariff = request.POST.get("tariff",False)
    unitMon1 = request.POST.get("unitMon1",False)
    unitMon2 = request.POST.get("unitMon2",False)
    unitMon3 = request.POST.get("unitMon3",False)
    supMon1 = request.POST.get("supMon1",False)
    supMon2 = request.POST.get("supMon2",False)
    supMon3 = request.POST.get("supMon3",False)

    payment_info = paymentDetails(fName=fName,lName=lName,email=email,phone=phone,address=address,address2=address2,
                                  city=city,AccNo=AccNo,tariff=tariff,unitMon1=unitMon1,unitMon2=unitMon2,unitMon3=unitMon3,supMon1=supMon1,supMon2=supMon2,supMon3=supMon3)
    payment_info.save()
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

