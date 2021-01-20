from django.shortcuts import render
from .froms import TicketForm
from .models import Ticket
from .services import AirService

# Create your views here.
def reservation(request):
    AirService().reservation(request)
    return render(request, 'reservation.html')

# 조건에 맞는 가는편 항공권 출력
def searchList_go(request):
    search_check = TicketForm(request.POST)
    context = AirService().searchList_go(search_check)
    return render(request, 'searchList_go.html', context)

# 조건에 맞는 오는편 항공권 출력
def searchList_come(request):
    search_check = TicketForm(request.POST)
    context = AirService().searchList_come(search_check)
    return render(request, 'searchList_come.html', context)