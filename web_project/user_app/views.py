from django.shortcuts import render

# Create your views here.
def loginViews(request):
    return render(request, 'login.html')

def signupViews(request):
    return render(request, 'signup.html')