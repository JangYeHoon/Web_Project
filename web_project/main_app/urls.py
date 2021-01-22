from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.indexViews, name='index'),
    path('specials_tickets',views.specials_tickets,name="specials_tickets"),
]