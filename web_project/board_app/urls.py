from django.urls import path, include
from . import views

urlpatterns = [
    path('board_list', views.board_list, name='board_list'),
    path('board_input', views.board_input, name='board_input'),
    path('board_add', views.board_add, name='board_add'),
    path('board_view', views.board_view, name='board_view'),
    path('board_modify_input', views.board_modify_input, name='board_modify_input'),
    path('board_modify', views.board_modify, name='board_modify'),
    path('board_delete', views.board_delete, name='board_delete'),
    path('comment_add', views.comment_add, name='comment_add'),
    path('loginStateCheck', views.loginStateCheck, name='loginStateCheck'),
]