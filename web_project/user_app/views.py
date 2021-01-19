from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponseRedirect

# Create your views here.
def loginViews(request):
    return render(request, 'login.html')

def signupViews(request):
    return render(request, 'signup.html')

def userCheck(request):
    new_user = UserForm(request.POST)
    #new_user.save()
    return HttpResponseRedirect('/')