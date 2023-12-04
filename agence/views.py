from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView, View
from .models import Room, Reservation
from .forms import AvailabilityForm
from agence.reservation_functions.availability import check_availability

# Create your views here.


class RoomListView(ListView):
    model = Room


class ReservationList(ListView):
    model = Reservation


class RoomDetailView(View):
    def get(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        form = AvailabilityForm()
        room_list = Room.objects.filter(category=category)
        
        if len(room_list) > 0:
            room = room_list[0]
            room_category = dict(room.Room_Categories).get(room_category, None)
            context = {
                'room_category': room_category,
                'form': form,
            }
            return render(request, 'room_detail_view.html', context)
        else:
            return HttpResponse('Category does not exist')

    def post(self, request, *args, **kwargs):
        category = self.kwargs.get('category', None)
        room_list = Room.objects.filter(category=category)
        form = AvailabilityForm(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
                
        if len(available_rooms) > 0:
            room = available_rooms[0]
            reservation = Reservation.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out'],
            )
            reservation.save()
            return HttpResponse(reservation)
        else:
            return HttpResponse('All of this category if rooms are booked! Try another one')


class ReservationView(FormView):
    form_class = AvailabilityForm
    template_name = "availability_form.html"

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
                
        if len(available_rooms) > 0:
            room = available_rooms[0]
            reservation = Reservation.objects.create(
                user=self.request.user,
                room=room,
                check_in=data['check_in'],
                check_out=data['check_out'],
            )
            reservation.save()
            return HttpResponse(reservation)
        else:
            return HttpResponse('All of this category if rooms are booked! Try another one')