from django.core.exceptions import ObjectDoesNotExist
from .models import Ticket

class AirService:
    def searchList_go(self, search_check):
        airline_list = Ticket.objects.filter(departure_place=search_check.data['departure_place'], arrival_place=search_check.data['arrival_place'], departure_data=search_check.data['departure_data'])
        seat = search_check.data['seat']
        read_date = search_check.data['departure_data']
        date = read_date.split("-")
        context = {"airline_list":airline_list, "date_month":date[1], "date_day":date[2], "arrival_date":search_check.data['arrival_data'], "seat":seat}
        return context

    def searchList_come(self, search_check):
        airline_list = Ticket.objects.filter(departure_place=search_check.data['departure_place'], arrival_place=search_check.data['arrival_place'], departure_data=search_check.data['departure_data'])
        go_airline = Ticket.objects.get(id=search_check.data['go_id'])
        seat = search_check.data['seat']
        read_date = search_check.data['departure_data']
        date = read_date.split("-")
        context = {"airline_list":airline_list, "date_month":date[1], "date_day":date[2], "seat":seat, "go_airline":go_airline}
        return context