from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    

class Vehicle(models.Model):
    #vehicle_id = models.AutoField()  # Auto-incrementing primary key
    vehicle_name = models.CharField(max_length=100)
    no_of_seats = models.PositiveIntegerField()
    price_for_eachday = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.vehicle_name
class booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    mobilenumber = models.CharField(max_length=10)
    no_of_days = models.IntegerField()
    name_of_car= models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    date_of_booking = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
    ]
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

class Payment(models.Model):
    card_number = models.CharField(max_length=16)
    expiration_date = models.CharField(max_length=5)
    cvv = models.CharField(max_length=3)
    name_on_card = models.CharField(max_length=100)
    #amount_to_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment for {self.name_on_card}"

    # You can add any additional methods or logic as needed

    