from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import EmployeeDetail

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EmployeeDetails(forms.Form):
    emp_name = forms.CharField(max_length=20, label='Employee Name :')
    emp_department = forms.CharField(max_length=20, label='Department : ')
    emp_email = forms.EmailField(label='E-Mail : ')
    phone = forms.IntegerField(label='Phone Number : ')

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = EmployeeDetail
        fields = '__all__'