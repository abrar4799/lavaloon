from rest_framework import  serializers

from ..models import Play , PlayBooking


class PlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Play
        fields = '__all__'


class PlayBookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayBooking
        fields = ['id', 'user', 'play', 'play_date', 'created_date']

