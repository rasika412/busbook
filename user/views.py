from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import FormView
from django.http import HttpResponse
from.models import rout_detailes,Bus_booking,Main_routes,User
from datetime import datetime
from .forms import BookingForm
from django import forms
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.views.generic import TemplateView
from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib import auth
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserform
from django.forms import inlineformset_factory
from django.contrib.auth import authenticate,login

  


# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request, 'about.html')

def feedback(request):
    return render(request, 'feedback.html')

def service(request):
    dict_city={
        'city':Main_routes.objects.all()
    }
    return render(request, 'service.html',dict_city)


def rout_dt(request,val):
    root=rout_detailes.objects.filter(city_2 = val)
    return render(request,'rout-detailes.html',locals())


def booking(request,val):
    form =  BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'booked'+user)
            root=rout_detailes.objects.filter(city_2 = val)
            return render(request,'try.html',locals())
    context = {'form':form}
    return render(request,'booking.html',context)


def confirmation(request):
    return render(request, 'confirmation.html')
def payment(request,val):
    city_3 = Main_routes.objects.filter(city_name = val)
    root=rout_detailes.objects.filter(city_2 = val)
    return render(request,'try.html',locals())
        
def registerPage(request):
    form = CreateUserform()
    if request.method == 'POST':
        form = CreateUserform(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created'+user)
            return redirect('login')
    context = {'form':form}
    return render(request,'register.html',context)
       
       
def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user is not  None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')
            return render(request,'index.html')
    return render(request,'index.html')
       
