from django import forms
from .models import Employee
from .models import Time

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = "__all__"


