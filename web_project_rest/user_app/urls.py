from django.urls import path
from . import views

urlpatterns = [
    path('',views.userList , name="users"),
    path('create/',views.userCreate , name="create"),
    path('login/',views.loginCheck , name="login"),
    path('logout/',views.logout, name="logout"),
    path('idcheck/<str:email>/',views.id_overlap_check , name="idcheck"),
]