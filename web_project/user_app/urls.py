from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.loginViews, name='login'),
    path('signup', views.signupViews, name='signup'),
    path('userCheck', views.userCheck, name='userCheck'),
    path('loginCheck', views.loginCheck, name='loginCheck'),
]