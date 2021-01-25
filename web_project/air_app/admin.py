from django.contrib import admin
from .models import Airline, Ticket

# Register your models here.
admin.site.register(Airline)
admin.site.register(Ticket)