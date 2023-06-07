from django.db import models


class Elevator(models.Model):
    elevator_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=30,
                              choices=(('Working', 'Working'), ('Under_Maintenance', 'Under_Maintenance')))
    current_floor = models.IntegerField()
    direction = models.CharField(max_length=30, choices=(('Upward', 'Upward'), ('Downward', 'Downward')))
    doors_open = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class ElevatorRequest(models.Model):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE)
    floor = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Elevator: {self.elevator.name}, Floor: {self.floor}"