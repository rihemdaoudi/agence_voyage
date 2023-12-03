from django.contrib import admin

from agence.models import  Hotel, Reservation, Room

# Register your models here.

admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(Reservation)