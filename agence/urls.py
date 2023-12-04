from django.urls import path
from .views import ReservationView, RoomList, ReservationList, RoomDetailView

app_name='agence'

urlpatterns = [
    path('room_list/', RoomList.as_view() , name='RoomList'),
    path('reservation_list/', ReservationList.as_view() , name='ReservationList'),
    path('book/', ReservationView.as_view(), name='ReservationView'),
    path('room/<category>', RoomDetailView.as_view(), name='roomDetail_view'),

    # path('login', views.login , name='login'),
    # path('register', views.register , name='register'),
    
]
