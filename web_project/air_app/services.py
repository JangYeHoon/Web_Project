from django.core.exceptions import ObjectDoesNotExist
from .models import Ticket, Reservation, Airline
from user_app.models import User
import random

class AirService:
    def searchList_go(self, search_check):
        airline_list = Ticket.objects.filter(departure_place=search_check.data['departure_place'], arrival_place=search_check.data['arrival_place'], departure_data=search_check.data['departure_data'])
        seat = search_check.data['seat']
        adult = search_check.data['adult']
        children = search_check.data['children']
        if children == '':
            children = 0
        section = search_check.data['section']
        read_date = search_check.data['departure_data']
        date = read_date.split("-")
        context = {"airline_list":airline_list, 'departure_data':read_date, 'departure_place':search_check.data['departure_place'], 'arrival_place':search_check.data['arrival_place'] ,"date_month":date[1], "date_day":date[2], "arrival_date":search_check.data['arrival_data'], "seat":seat, "adult":adult, "children":children, "section":section}
        return context

    def searchList_come(self, search_check):
        airline_list = Ticket.objects.filter(departure_place=search_check.data['departure_place'], arrival_place=search_check.data['arrival_place'], departure_data=search_check.data['departure_data'])
        go_airline = Ticket.objects.get(id=search_check.data['go_id'])
        seat = search_check.data['seat']
        adult = search_check.data['adult']
        children = search_check.data['children']
        read_date = search_check.data['departure_data']
        date = read_date.split("-")
        context = {"airline_list":airline_list, 'departure_data':read_date, 'departure_place':search_check.data['departure_place'], 'arrival_place':search_check.data['arrival_place'], "date_month":date[1], "date_day":date[2], "seat":seat, "go_airline":go_airline, "adult":adult, "children":children}
        return context

    def reservation_add(self, request):
        user_id = request.session.get('login_id')
        check_user = False
        if user_id:
            user = User.objects.get(email=user_id)
            check_user = True
        
        go_airline_id = request.POST['go_id']
        go_airline = Ticket.objects.get(id=go_airline_id)

        seat = request.POST['seat']
        adult = request.POST['adult']
        children = request.POST['children']
        go_price = 0
        come_price = 0

        section = request.POST['section']
        if section == 'round_trip':
            come_airline_id = request.POST['come_id']
            come_airline = Ticket.objects.get(id=come_airline_id)

            if seat == '1':
                go_price = go_airline.economy_price
                come_price = come_airline.economy_price
            elif seat == '2':
                go_price = go_airline.premium_price
                come_price = come_airline.premium_price
            elif seat == '3':
                go_price = go_airline.business_class_price
                come_price = come_airline.business_class_price
            elif seat == '4':
                go_price = go_airline.first_class_price
                come_price = come_airline.first_class_price
            price = (go_price + come_price) * int(adult) + ((go_price + come_price) * 0.9) * int(children)
            if check_user == True:
                new_reservation = Reservation(user_id=user, go_ticket_id=go_airline, come_ticket_id=come_airline, price=price)
        elif section == 'one_way':
            if seat == '1':
                go_price = go_airline.economy_price
            elif seat == '2':
                go_price = go_airline.premium_price
            elif seat == '3':
                go_price = go_airline.business_class_price
            elif seat == '4':
                go_price = go_airline.first_class_price
            price = go_price * int(adult) + (go_price * 0.9) * int(children)
            if check_user == True:
                new_reservation = Reservation(user_id=user, go_ticket_id=go_airline, come_ticket_id=None, price=price)
        if check_user == True:
            new_reservation.save()
            context = {"new_reservation":new_reservation}
        else:
            if section == 'round_trip':
                context = {"go_ticket_id":go_airline_id, "come_ticket_id":come_airline_id, "price":price, "section":section}
            elif section == 'one_way':
                context = {"go_ticket_id":go_airline_id, "price":price, "section":section}
        return context, check_user

    def reservation_list(self, request):
        user_id = request.session.get('login_id')
        if user_id:
            user = User.objects.get(email=user_id)
        else:
            return False
        reservation_list = Reservation.objects.filter(user_id=user)
        context = {"reservation_list":reservation_list}
        return context

    def reservation_cancel(self, reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)
        reservation.delete()

    def db_insert(self):
        airline_id = 1
        for i in range(1, 11, 1):
            # hour = random.randint(7, 21)
            # minute = random.randint(0, 50)
            # start_time = str(hour) + ":" + str(minute)
            # end_time = str(hour+1) + ":" + str(minute+5)
            # first_price = random.randint(180000, 200000)
            # business_price = random.randint(150000, 180000)
            # premium_price = random.randint(110000, 150000)
            # economy_price = random.randint(70000, 110000)
            # new_ticket = Ticket(airline_id_id=airline_id, departure_place='제주', arrival_place='서울', departure_airport='CJU', arrival_airport='GMP',
            # departure_time=start_time, arrival_time=end_time, departure_data='2021-02-04', first_class_price=first_price, business_class_price=business_price,
            # premium_price=premium_price, economy_price=economy_price)

            # hour = random.randint(7, 21)
            # minute = random.randint(5, 55)
            # start_time = str(hour) + ":" + str(minute)
            # end_time = str(hour+1) + ":" + str(minute-5)
            # first_price = random.randint(800000, 1000000)
            # business_price = random.randint(750000, 800000)
            # premium_price = random.randint(700000, 750000)
            # economy_price = random.randint(650000, 700000)
            # new_ticket = Ticket(airline_id_id=airline_id, departure_place='상하이', arrival_place='서울', departure_airport='PVG', arrival_airport='ICN',
            # departure_time=start_time, arrival_time=end_time, departure_data='2021-02-04', first_class_price=first_price, business_class_price=business_price,
            # premium_price=premium_price, economy_price=economy_price)

            hour = random.randint(7, 21)
            minute = random.randint(0, 40)
            start_time = str(hour) + ":" + str(minute)
            end_time = str(hour+2) + ":" + str(minute+15)
            first_price = random.randint(340000, 370000)
            business_price = random.randint(320000, 340000)
            premium_price = random.randint(300000, 320000)
            economy_price = random.randint(260000, 300000)
            new_ticket = Ticket(airline_id_id=airline_id, departure_place='도쿄', arrival_place='서울', departure_airport='NRT', arrival_airport='ICN',
            departure_time=start_time, arrival_time=end_time, departure_data='2021-02-04', first_class_price=first_price, business_class_price=business_price,
            premium_price=premium_price, economy_price=economy_price)
            new_ticket.save()
            if i % 2 == 0:
                airline_id += 1