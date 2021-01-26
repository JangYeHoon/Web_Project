from django.shortcuts import render
from .forms import TicketForm
from .models import Ticket, Reservation
from .services import AirService
from django.http import HttpResponseRedirect
from django.urls import reverse

# 예약 추가
def reservation_add(request):
    # if not request.session.get('login_id') :
    #     return HttpResponseRedirect('/user_app/login')
    context, check_user = AirService().reservation_add(request)
    if check_user == False:
        return render(request, 'login.html', context)
    return render(request, 'reservation_complete.html', context)

# 예약 리스트 출력
def reservation_list(request):
    context = AirService().reservation_list(request)
    if context == False:
        return HttpResponseRedirect('/user_app/login')
    return render(request, 'reservation_list.html', context)

# 예약 삭제
def reservation_cancel(request):
    reservation_id = request.POST['reservation_id']
    AirService().reservation_cancel(reservation_id)
    return HttpResponseRedirect(reverse('reservation_list'))

# 조건에 맞는 가는편 항공권 출력
def searchList_go(request):
    search_check = TicketForm(request.POST)
    context = AirService().searchList_go(search_check)
    return render(request, 'searchList_go.html', context)

def searchList_go_get(request):
    search_check = TicketForm(request.GET)
    context = AirService().searchList_go(search_check)
    return render(request, 'searchList_go.html', context)

# 조건에 맞는 오는편 항공권 출력
def searchList_come(request):
    search_check = TicketForm(request.POST)
    context = AirService().searchList_come(search_check)
    return render(request, 'searchList_come.html', context)