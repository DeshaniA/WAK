from django import forms
from .models import Supplier
from .models import Product
from .models import Contract
from .models import Rating


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = "__all__"


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = "__all__"