from django.shortcuts import render
from .services import MainService
from django.http import JsonResponse

# Create your views here.
def indexViews(request):
    context = MainService().searchPlace()
    return render(request, 'index.html',context)

def specials_tickets(request):
    airline_id = request.GET.get('airline_id')

    tickets = MainService().specials_tickets(airline_id)
    result = tickets
    return JsonResponse(result,safe=False)
