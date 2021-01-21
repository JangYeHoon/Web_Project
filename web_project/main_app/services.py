from django.core.exceptions import ObjectDoesNotExist
from air_app.models import Ticket
from air_app.models import Reservation

class MainService:
    def searchPlace(self):
        departure_place_list= Ticket.objects.all().values('departure_place').distinct().order_by('departure_place')
        arrival_place_list = Ticket.objects.all().values('arrival_place').distinct().order_by('arrival_place')
        reservation_list = Reservation.objects.filter(come_ticket_id__isnull=False)
        dic = {}
        dic_place = {}
        ranking_list = []
        for reservation in reservation_list:
            go_str = reservation.go_ticket_id.departure_place + reservation.go_ticket_id.arrival_place
            come_str = reservation.go_ticket_id.arrival_place + reservation.go_ticket_id.departure_place
            if go_str not in dic and come_str not in dic:
                dic[go_str] = 1
                dic_place[go_str] = reservation
            else:
                if go_str in dic:
                    dic[go_str] += 1
                elif come_str in dic:
                    dic[go_str] += 1
        sorted_dic = sorted(dic.items(), reverse=True, key=lambda item:item[1])
        
        for key in sorted_dic:
            for place_key in dic_place:
                if place_key == key[0]:
                    ranking_list.append(dic_place.get(place_key))
        context ={"departure_place_list":departure_place_list,"arrival_place_list":arrival_place_list, "ranking_list":ranking_list}
        return context