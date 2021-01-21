from django.urls import path, include
from . import views

urlpatterns = [
    path('login', views.loginViews, name='login'),
    path('signup', views.signupViews, name='signup'),
    path('userCheck', views.userCheck, name='userCheck'),
    path('loginCheck', views.loginCheck, name='loginCheck'),
    path('logout',views.logout,name='logout'),
    path('id_overlap_check',views.id_overlap_check,name='id_overlap_check'),
]