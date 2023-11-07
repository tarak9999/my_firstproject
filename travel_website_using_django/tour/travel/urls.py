from django.urls import path
from travel import views
from django.views.generic.base import RedirectView
urlpatterns = [
    path('',RedirectView.as_view(url="home/")),
    
    path('home/',views.home,name='travel-home'),
    path('about/',views.about),
    path('tour/',views.tour ),
    path('vehicles/',views.vehicles),
    path('book_now/',views.book_now),
    path('payment1/',views.payment),
    path('register/',views.register),
    path('profile/',views.profile),
    path('mybooking/',views.mybooking,name='mybooking'),
    #path('login/',views.login),
   
]
