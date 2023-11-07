from django.shortcuts import render,redirect
from django.core.mail import send_mail
from tour import settings
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *


# from django.http.response import HttpResponse

# Create your views here.
def home(req):
    return render(req,"homepage.html")
@login_required
def book_now(req):
    if req.method=="POST":
        Fname=req.POST['firstname']
        mobile_number=req.POST['mobile number']
        to=req.POST['no_of_days']
        Date=req.POST['date']
        vehicle=req.POST['Vehicle']
        category=req.POST['category']
        vehicle=Vehicle.objects.get(vehicle_name =vehicle)
        # str1='Name-'+Fname+"\n"+'Mobile Number-'+mobile_number+"\n"+'Destination-'+to+"\n"+'Date-'+Date+"\n"+'Vehicle-'+vehicle+"\n"+'Category-'+category
        url = f'/travel/payment1/?mobile_number={mobile_number}'
        booking(mobilenumber = mobile_number,no_of_days=to,name_of_car =vehicle).save()
        return HttpResponseRedirect(url)
        # return redirect('/travel/payment1')
    return render(req,"book_now.html")
def payment(req):
    if req.method=="POST":
        form = PaymentForm(req.POST)
        if form.is_valid():
            name = req.user
            object = name.booking_set.last()
            object.status  =  'Accepted'
            object.save()
            print(object.status)
            return redirect('travel-home')   
    a = req.GET.get('mobile_number')
    x = booking.objects.filter(mobilenumber=a).last().name_of_car
    total = (booking.objects.filter(mobilenumber=a).last().no_of_days)*(Vehicle.objects.filter(vehicle_name=x).last().price_for_eachday)
    form = PaymentForm()
    return render(req,"payment1.html",{'total':total,'form':form})
def about(req):
    return render(req,"about.html")
def tour(req):
    return render(req,"tour.html")
def vehicles(req):
    return render(req,"vehicles.html")
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
@login_required
def profile(request):
    return render(request, 'profile.html')

def mybooking(request):
    name = request.user
    mybook = name.booking_set.filter(status='Accepted')
    return render(request, 'mybooking.html',{'mybook':mybook})
