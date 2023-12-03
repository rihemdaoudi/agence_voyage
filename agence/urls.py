from django.urls import path
from . import views
from .views import Roomlist, ReservationList

app_name='agence'

urlpatterns = [
    path('room_list/', Roomlist.as_view() , name='RoomList'),
    path('reservation_list/', ReservationList.as_view() , name='ReservationList'),
    # path('', views.home_view , name='home'),
    # path('login', views.login , name='login'),
    # path('register', views.register , name='register'),
    
]
