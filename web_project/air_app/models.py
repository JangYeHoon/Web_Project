from django.db import models
from user_app.models import User

# Create your models here.
class Airline(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50)  # 항공사 이름
    air_img = models.FileField(upload_to='air_imag/')   # 항공사 이미지 경로

class Ticket(models.Model):
    objects = models.Manager()
    airline_id = models.ForeignKey(Airline, on_delete=models.CASCADE, related_name="ticket")   # 항공사 외래키
    departure_place = models.CharField(max_length=50)  # 출발지
    arrival_place = models.CharField(max_length=50)    # 도착지
    departure_airport = models.CharField(max_length=10)    # 출발공항(공항코드)
    arrival_airport = models.CharField(max_length=10)  # 도착공항(공항코드)
    departure_time = models.TimeField()    # 출발시간
    arrival_time = models.TimeField()   # 도착시간
    departure_data = models.DateField() # 출발날짜
    first_class_price = models.IntegerField()   # 일등석 가격
    business_class_price = models.IntegerField()    # 비즈니스 가격
    premium_price = models.IntegerField()   # 프리미엄 가격
    economy_price = models.IntegerField()   # 일반석 가격

class Reservation(models.Model):
    objects = models.Manager()
    user_id = models.ForeignKey(User, on_delete = models.CASCADE, related_name="reservation")   # 유저 외래키
    go_ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="go_ticket", null=True)  # 가는편 외래키
    come_ticket_id = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="come_ticket", null=True)    # 오는편 외래키
    reservation_date = models.DateField(auto_now_add=True)   # 예약날짜
    price = models.IntegerField()   # 결제금액