from rest_framework import serializers, viewsets
from .models import Airline, Ticket, Reservation

class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['name', 'air_img']

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['airline_id', 'departure_place', 'arrival_place', 'departure_airport', 'arrival_airport',
            'departure_time', 'arrival_time', 'departure_date', 'first_class_price', 'business_class_price',
            'premium_price', 'economy_price']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['user_id', 'go_ticket_id', 'come_ticket_id', 'reservation_date', 'price']