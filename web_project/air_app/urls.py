from django.urls import path, include
from . import views

urlpatterns = [
    path('reservation_add', views.reservation_add, name='reservation_add'),
    path('reservation_list', views.reservation_list, name='reservation_list'),
    path('searchList_go', views.searchList_go, name='searchList_go'),
    path('searchList_go_get', views.searchList_go_get, name='searchList_go_get'),
    path('searchList_come', views.searchList_come, name='searchList_come'),
    path('reservation_cancel', views.reservation_cancel, name='reservation_cancel'),
]
