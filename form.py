from django import forms
from .models import Employee
from .models import Time
from .models import Salary

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = "__all__"


class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = "__all__"