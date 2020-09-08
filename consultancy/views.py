from  django.http import Http404
from django.shortcuts import render, get_object_or_404


# Create your views here.
from .models import cusStatus


def domestic_reg_cust_page(request,post_id):
    obj = get_object_or_404(cusStatus, id = post_id)
    template_name = 'domestic_reg_cust_page.html'
    context = {"object": obj}
    return render(request, template_name, context)
