from django.urls import path
from . import views

urlpatterns = [
    path('',views.board_list , name="board"),
    path('add/',views.board_add , name="add"),
    path('view/<str:pk>/',views.board_view, name="view"),
    path('modifyinput/<str:pk>/',views.board_modify_input, name="modifyinput"),
    path('modify/<str:pk>/',views.board_modify, name="modify"),
    path('delete/<str:pk>/',views.board_delete, name="delete"),
    path('commentadd/',views.comment_add, name="commentadd"),
    path('commentdelete/<str:pk>/',views.comment_delete, name="commentdelete"),
]