from django.core.exceptions import ObjectDoesNotExist
from air_app.models import Ticket, Reservation, Airline
from django.db.models import Model, Min

class MainService:
    def searchPlace(self):
        # 항공권 검색시 티켓이 있는 장소 검색
        departure_place_list= Ticket.objects.all().values('departure_place').distinct().order_by('departure_place')
        arrival_place_list = Ticket.objects.all().values('arrival_place').distinct().order_by('arrival_place')

        # 인기 항공권
        ranking_list = self.popular_ticket()
        
        # 항공사별 특가 티켓
        airline_list =self.specials_tickets_airline()
        tickets= self.specials_tickets(airline_list[0].id)

        context ={"departure_place_list":departure_place_list,"arrival_place_list":arrival_place_list, "ranking_list":ranking_list, "tickets":tickets, "airline_list":airline_list}
        return context   

    def popular_ticket(self):
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
        return ranking_list

    def specials_tickets_airline(self):
         airline = Airline.objects.all()

         return airline

    def specials_tickets(self, airline_id):
        tickets = Ticket.objects.filter(airline_id_id=airline_id).values('airline_id_id', 'departure_place', 'arrival_place').annotate(Min('economy_price')).values('airline_id_id', 'departure_place', 'arrival_place', 'departure_data', 'economy_price')
        return tickets