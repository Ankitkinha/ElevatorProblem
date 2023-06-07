from django.contrib import admin

# Register your models here.
from elevator_app.models import Elevator, ElevatorRequest

admin.site.register(Elevator)
admin.site.register(ElevatorRequest)
