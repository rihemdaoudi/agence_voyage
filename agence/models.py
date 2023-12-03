from django.db import models
from django.conf import settings
#import datetime
# Create your models here.
class Room(models.Model):
    Room_Categories = (
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )  
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=Room_Categories)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    
    def __str__(self): 
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'
    
# """ class Client(models.Model):
#     nom = models.CharField(max_length=100)
#     prenom = models.CharField(max_length=100)
#     phone = models.CharField(x_length=100)
#     email = models.EmailField(max_length=100)
#     password = models.CharField(max_length=100)
#     age = models.IntegerField()
    
#     def __str__(self):
#         return f'{self.nom} {self.prenom}' """
    
class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField()
    
    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'


class Hotel(models.Model):
        nom = models.CharField(max_length=255)
        description = models.TextField(default="",blank=True)
        prix = models.DecimalField(max_digits=6, decimal_places=2)
        # image =models.ImageField()
