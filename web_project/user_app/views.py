from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .services import UserService
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.
def loginViews(request):
    return render(request, 'login.html')

def signupViews(request):
    return render(request, 'signup.html')

def userCheck(request):
    new_user = UserForm(request.POST)
    new_user.save()
    return HttpResponseRedirect('/')

def loginCheck(request):
    user_id = request.POST['email']
    user_pw = request.POST['password']
    result = UserService().loginCheck(user_id, user_pw)
    if result == True:
        forward_reservaion = request.POST['forward_reservaion']
        request.session['login_id'] = user_id
        if forward_reservaion == '1':
            context = UserService().reservation_login(user_id, request)
            return render(request, 'reservation_complete.html', context)
        else:
            return HttpResponseRedirect('/')
    else:
        messages.add_message(request, messages.INFO, '등록된 ID가 없거나 비밀번호가 다릅니다.')
        return render(request, 'login.html')

def logout(request):
    request.session.modidied = True
    del request.session['login_id']
    return HttpResponseRedirect('/')
    

    
def id_overlap_check(request):
    email = request.GET.get('email')

    user = UserService().id_overlap_check(email)

    if user is None:
        overlap = "pass"
    else:
        overlap = "fail"

    context = {'overlap':overlap}
    return JsonResponse(context)
