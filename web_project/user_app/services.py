from .models import User
from django.core.exceptions import ObjectDoesNotExist
from air_app.models import Reservation, Ticket

class UserService:
    def loginCheck(self, user_id, user_pw):
        try:
            user = User.objects.get(email = user_id)
            if user_pw == user.password:
                
                return True
            else:
                return False
        except ObjectDoesNotExist:
            return False
        except:
            return False

    def reservation_login(self, user_id, request):
        user = User.objects.get(email = user_id)
        go_ticket_id = request.POST['go_ticket_id']
        go_airline = Ticket.objects.get(id=go_ticket_id)
        section = request.POST['section']
        price = request.POST['price']
        if section == 'round_trip':
            come_ticket_id = request.POST['come_ticket_id']
            come_airline = Ticket.objects.get(id=come_ticket_id)
            new_reservation = Reservation(user_id=user, go_ticket_id=go_airline, come_ticket_id=come_airline, price=int(price))
        elif section == 'one_way':
            new_reservation = Reservation(user_id=user, go_ticket_id=go_airline, come_ticket_id=None, price=int(price))
        new_reservation.save()
        price = int(price)
        context = {"new_reservation":new_reservation, "price":price}
        return context
    
    def id_overlap_check(self,email):
        try:
            user = User.objects.get(email = email)
            print(user.email)
            return user
        except:
            user = None
            return user