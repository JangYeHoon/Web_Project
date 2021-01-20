from django.shortcuts import render
from .services import MainService

# Create your views here.
def indexViews(request):
    context = MainService().searchPlace()
    return render(request, 'index.html',context)

