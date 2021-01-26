from django.urls import path, include
from . import views

urlpatterns = [
    path('board_list', views.board_list, name='board_list'),
]