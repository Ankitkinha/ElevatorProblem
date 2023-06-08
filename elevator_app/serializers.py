from rest_framework import serializers

from elevator_app.models import Elevator, ElevatorRequest


class ElevatorSerializer(serializers.ModelSerializer):
    elevator_id = serializers.ReadOnlyField()

    class Meta:
        model = Elevator
        fields = "__all__"


class ElevatorRequestSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = ElevatorRequest
        fields = "__all__"
