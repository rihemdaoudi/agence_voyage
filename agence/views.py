from django.shortcuts import render
from django.views.generic import ListView
from .models import Room , Reservation
# Create your views here.

class Roomlist(ListView):
    model=Room
class ReservationList(ListView):
    model = Reservation
    
# def home_view(request):
#     return render(request,'home.html', {})

# def login(request):
#     return render(request, 'login.html')

# def register(request):
#     return render(request,'register.html')
