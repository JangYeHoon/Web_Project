from django.forms import ModelForm
from .models import Ticket

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = {'id', 'departure_place', 'arrival_place', 'departure_airport',
        'arrival_airport', 'departure_time', 'arrival_time', 'departure_data', 'first_class_price',
        'business_class_price', 'premium_price', 'economy_price'}