from django.urls import path, include
from . import views

urlpatterns = [
    path('reservation_add', views.reservation_add, name='reservation_add'),
    path('reservation_list', views.reservation_list, name='reservation_list'),
    path('searchList_go', views.searchList_go, name='searchList_go'),
    path('searchList_come', views.searchList_come, name='searchList_come'),
]
