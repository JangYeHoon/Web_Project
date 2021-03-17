from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .airdto import AirlineSerializer, TicketSerializer, ReservationSerializer
from .models import Airline, Ticket, Reservation
from user_app.models import User

# Create your views here.
# 예약 추가
@api_view(['POST'])
def reservationAdd(request):
    serializer = ReservationSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

# 예약 리스트 출력
@api_view(['GET'])
def reservationList(request, user_id):
    user = User.objects.get(id=user_id)
    reservations = Reservation.objects.filter(user_id=user)
    serializer = ReservationSerializer(reservations, many = True)
    return Response(serializer.data)

# 예약 삭제
@api_view(['DELETE'])
def reservationCancel(request, pk):
    reservation = Reservation.objects.get(id = pk)
    reservation.delete()
    return Response('Deleted')

# 조건에 맞는 항공권 출력
@api_view(['PUT'])
def searchList(request, price):
    if request.data['order'] == "1":
        ticket = Ticket.objects.filter(departure_place=request.data['departure_place'], arrival_place=request.data['arrival_place'], departure_date=request.data['departure_date']).order_by(price)
        # ticket = Ticket.objects.all()
    elif request.data['order'] == "2":
        ticket = Ticket.objects.filter(departure_place=request.data['departure_place'], arrival_place=request.data['arrival_place'], departure_date=request.data['departure_date']).order_by('departure_time')
    elif request.data['order'] == "3":
        ticket = Ticket.objects.filter(departure_place=request.data['departure_place'], arrival_place=request.data['arrival_place'], departure_date=request.data['departure_date']).order_by('-departure_time')
    else:
        ticket = Ticket.objects.all()
    serializer = TicketSerializer(ticket, many = True)
    return Response(serializer.data)