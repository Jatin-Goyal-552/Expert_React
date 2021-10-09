from django.shortcuts import render
from .forms import CreateUserForm
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import collections
import pandas as pd
import csv
from django.core.mail import send_mail
from django.conf import settings
import numpy as np
from django.urls import reverse_lazy
from .models import *
from .forms import AddLinkForm
from django.views.generic import DeleteView



# Create your views here.
def register(request):
    global username,email,password,OTP
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password1')
            print("email",email)
            OTP = np.random.randint(100000, 999999)
            email_subject = "OTP varification for Your account"
            email_body = "Thanks for showing intrest in Survelon Series products. OTP for your account is {}".format(OTP)
            print(send_mail( email_subject, email_body, settings.EMAIL_HOST_USER, [email], fail_silently=False))
            return render(request, 'otp2.html')
            # form.save()
            # user = form.cleaned_data.get('username')
            # messages.success(request, 'Account was created for ' + user)
            # return redirect('login')
    context = {'form':form}
    return render(request, 'register.html', context)

def check_otp(request):
    if request.method == 'POST':
        otp = request.POST['otp']
        print("OTP", otp)
        if OTP==int(otp):
            user = User.objects.create_user(username=username,email=email,password=password)
            user.save()
            print('user created')
            messages.info(request,"You are now registered... Please login to continue.")
            return redirect('login')
        else:
            messages.info(request,"OTP didn't match, Please register again.")
            return render(request, 'otp2.html')

def login1(request):
    if request.method == 'POST':
        username  = request.POST.get('your_name')
        print(username )
        password =request.POST.get('your_pass')
        print(password)
        user = authenticate(request,username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            if request.user.is_superuser:
                # internship=Internships.objects.all()
                # # print(internship[0].iid)
                # context={
                #     'name':request.user,
                #     'internships':internship,
                #     'user_id':request.user.id
                # }
                # print(context)
                # return render(request, 'admin_home.html',context)
                return redirect('admin_home')
            global name
            name=username
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
    
    return render(request,'login.html')

def logout1(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='login')
# def home(request):
#     # internship=Internships.objects.all()
#                 # print(internship[0].iid)
#     context={
#             'user_id':request.user.id
#                 }
#     print(context)
#     return render(request, 'home.html',context)

@login_required(login_url='login')
def home_view(request):
    no_discounted = 0
    error = None
    initial_data={  
                'user':request.user.id,
                'link':''
            }
    
    form = AddLinkForm(initial=initial_data)

    if request.method == 'POST':
        form = AddLinkForm(request.POST ,initial=initial_data)
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
            error = "Ups ... couldn't get the name or the price"
        except:
            error = "Ups ... something went wrong"
        return redirect('home')
    

    qs = Link.objects.all()
    items_no = qs.count()

    if items_no > 0:
        discount_list = []
        for item in qs:
            if item.old_price > item.current_price:
                discount_list.append(item)
            no_discounted = len(discount_list)

    context = {
        'qs': qs,
        'items_no': items_no,
        'no_discounted': no_discounted,
        'form': form,
        'error': error,
    }

    return render(request, 'main.html', context)

@login_required(login_url='login')
def delete(request,id):
    link=Link.objects.get(l_id=id)
    link.delete()
    return redirect('home')

@login_required(login_url='login')
def update_prices(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('home')