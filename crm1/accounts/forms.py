from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields = '__all__'
        exclude=['user', 'phone']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__' #Taking all the fields of that model
        #if we want certain fields we can make a list ['customer', 'order']
        exclude=['Customer']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']