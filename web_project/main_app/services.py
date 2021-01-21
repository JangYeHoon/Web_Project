from django.core.exceptions import ObjectDoesNotExist
from air_app.models import Ticket

class MainService:
    def searchPlace(self):
        departure_place_list= Ticket.objects.all().values('departure_place').distinct().order_by('departure_place')
        arrival_place_list = Ticket.objects.all().values('arrival_place').distinct().order_by('arrival_place')
        context ={"departure_place_list":departure_place_list,"arrival_place_list":arrival_place_list}
        print(departure_place_list)
        return context