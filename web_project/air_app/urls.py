from django.urls import path, include
from . import views

urlpatterns = [
    path('reservation_add', views.reservation_add, name='reservation_add'),
    path('searchList_go', views.searchList_go, name='searchList_go'),
    path('searchList_come', views.searchList_come, name='searchList_come'),
]
