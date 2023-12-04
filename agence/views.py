from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View
from .models import Room , Reservation
from .forms import AvailabilityForm
from agence.reservation_functions.availability import check_availability

# Create your views here.

class RoomListView(ListView):
    model=Room
    
class ReservationList(ListView):
    model = Reservation
    
class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        room_category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=room_category)
        room = room_category[0]
        
        context = {
            'room_category': room.category
        }
        return render(request, 'room_detail_view.html', context)
        
    
    def post(self, request, *args, **kwargs):
        room_category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms) > 0 :
            room = available_rooms[0]
            reservation = Reservation.objects.create(
                user=self.request.user,
                room=room,
                check_in = data['check_in'],
                check_out  = data['check_out']
            )
            reservation.save()
            return HttpResponse(reservation)
        else:
            return HttpResponse('All of this category if rooms are booked! Try another one')

class ReservationView(FormView):
    form_class = AvailabilityForm 
    template_name = 'availability_form.html'
    def  form_valid(self, form): 
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms=[]
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        if len(available_rooms) > 0:
            room = available_rooms[0]
            reservation = Reservation.objects.create(
                user = self.request.user,
                room = room,
                check_in=data['check_in'],
                check_out = data['check_out']
            )
            reservation.save()
            return HttpResponse(reservation)
        else:
            return HttpResponse('All of this category if rooms are booked! Try another one')
    
# def home_view(request):
#     return render(request,'home.html', {})

# def login(request):
#     return render(request, 'login.html')

# def register(request):
#     return render(request,'register.html')
