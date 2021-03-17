from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.reservationAdd , name="add"),
    path('reservation/<str:user_id>/',views.reservationList , name="reservation"),
    path('delete/<str:pk>/',views.reservationCancel, name="delete"),
    path('ticket/<str:price>/',views.searchList, name="ticket"),
]