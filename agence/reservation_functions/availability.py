import datetime 
from agence.models import Room, Reservation

def check_availability(room, check_in, check_out):
    available_list = []
    reservation_list = Reservation.objects.filter(room=room)
    for reservation in reservation_list:
        if reservation.check_in > check_out or reservation.check_out < check_in:
            available_list.append(True)
        else:
            available_list.append(False)
    return all(available_list)
    
    