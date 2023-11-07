from django.contrib import admin
from .models import *


class vehicleadmin(admin.ModelAdmin) :
    link_display= ('vehicle_name','no_of_seats','price_for_eachday')

admin.site.register(Profile)
admin.site.register(Vehicle,vehicleadmin)
admin.site.register(booking)