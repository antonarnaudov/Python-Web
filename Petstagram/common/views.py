from django import forms
from django.shortcuts import render


# Create your views here.
from common.models import User


def landing_page(request):
    return render(request, 'landing_page.html')


# class RegisterUserForm(forms.Form):
#     username = forms.CharField(label='Username')
#     first_name = forms.CharField(label='First Name')
#     surname = forms.CharField(label='Surname')
#     password = forms.CharField(label='Password')
#
#     def save(self):
#         username = self.cleaned_data['username']
#         first_name = self.cleaned_data['first_name']
#         surname = self.cleaned_data['surname']
#         password = self.cleaned_data['password']
#
#         user = User()

def register_form(request):
    return render(request, 'shared/register_form.html')


def login_form(request):
    return render(request, 'shared/login_form.html')
