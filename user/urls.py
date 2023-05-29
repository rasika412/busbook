from django.contrib import admin
from django.urls import path
from . import views
from django.urls import re_path as url
from user import views as user_view
from django.contrib.auth import views as auth
from django.contrib.auth import views as auth_views
from user import views as user_views



urlpatterns = [
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('feedback',views.feedback,name='feedback'),
    path('service',views.service,name='service'),
    path('detail/<slug:val>',views.rout_dt,name='detail'),
    path('booking/<slug:val>',views.booking,name='booking'),
    path('confirmation',views.confirmation,name='confirmation'),
    path('payment/<slug:val>',views.payment,name='payment'),
    path('regist',views.registerPage,name='regist'),
    path('',views.loginPage,name='login'),
    # path('paypa', views.try_payment, name='paypa'),
] 


