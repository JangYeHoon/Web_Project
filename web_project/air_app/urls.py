from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('reservation', views.reservation, name='reservation'),
    path('searchList_go', views.searchList_go, name='searchList_go'),
    path('searchList_come', views.searchList_come, name='searchList_come'),
]
