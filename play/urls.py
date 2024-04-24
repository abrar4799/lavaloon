from django.urls import  path
from .api.view import Booking

urlpatterns = [
    path('', Booking.as_view(), name='booking')
]