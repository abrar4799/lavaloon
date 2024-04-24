from django.db import transaction
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  status
from ..models import PlayBooking, Play, Seats

from .serializer import PlayBookingSerializer



class Booking(APIView):
    @transaction.atomic
    def post(self,request):
        serializer = PlayBookingSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            user_email = validated_data.get('user')
            play = validated_data.get('play')
            play_id = play.pk
            play_date = validated_data.get('play_date')
            try:
                if PlayBooking.objects.filter(user=user_email, play_date=play_date).exists():
                    return Response({'message': 'A booking already exists for this user and play date.'},
                                    status=status.HTTP_400_BAD_REQUEST)
                play = Play.objects.select_for_update().get(pk=play_id)
                seats = Seats.objects.select_for_update().get(play=play, play_date=play_date)
                if seats.remaining_seats > 0:
                    seats.remaining_seats -= 1
                    seats.save()

                    # Create the booking
                    booking = PlayBooking.objects.create(user=user_email, play=play, play_date=play_date)
                    serializer = PlayBookingSerializer(booking)
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'message': 'No available seats for this play on this date.'}, status=status.HTTP_400_BAD_REQUEST)

            except Play.DoesNotExist:
                return Response({'message': 'Play does not exist.'}, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
