from django.urls import path, include
from . import views

urlpatterns = [
    path('reservation', views.reservation, name='reservation'),
    path('searchList_go', views.searchList_go, name='searchList_go'),
    path('searchList_come', views.searchList_come, name='searchList_come'),
]
