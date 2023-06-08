from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from elevator_app.models import Elevator, ElevatorRequest
from elevator_app.serializers import ElevatorSerializer, ElevatorRequestSerializer


class ElevatorViewSet(viewsets.ModelViewSet):
    queryset = Elevator.objects.all()
    serializer_class = ElevatorSerializer

# API-1 (Initialise the elevator system to create ‘n’ elevators in the system)
    @action(detail=False, methods=['post'])
    def initialize_elevator_system(self, request):
        num_elevators = request.data.get('num_elevators')
        if not num_elevators:
            return Response({'message': 'Number of elevators is required'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            num_elevators = int(num_elevators)
        except ValueError:
            return Response({'message': 'Invalid number of elevators'}, status=status.HTTP_400_BAD_REQUEST)

        if num_elevators < 1:
            return Response({'message': 'Number of elevators must be at least 1'}, status=status.HTTP_400_BAD_REQUEST)

        elevators = []
        for _ in range(num_elevators):
            elevator = Elevator.objects.create()
            elevators.append(elevator)

        serializer = ElevatorSerializer(elevators, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# API-2 (Fetch all requests for a given elevator)
    @action(detail=True, methods=['get'])
    def get_elevator_requests(self, request, pk):
        try:
            elevator = Elevator.objects.get(elevator_id=pk)
        except Exception as e:
            return Response({'message': 'Elevator does not exist'})
        elevator_requests = ElevatorRequest.objects.filter(elevator=elevator)
        if not elevator_requests:
            return Response({'message': 'Elevator_request does not exist'})
        req_serializer = ElevatorRequestSerializer(
            elevator_requests, many=True, context={'request': request})
        return Response(req_serializer.data)

# API-3 (Fetch the next destination floor for a given elevator)
    @action(detail=True, methods=['get'])
    def get_elevator_next_destination_floor(self, request, elevator_id):
        try:
            elevator = Elevator.objects.get(elevator_id=elevator_id)
        except Exception as e:
            return Response({'message': 'Elevator does not exist'})
        next_floor = elevator.current_floor + 1
        return Response({'next_destination_floor': next_floor})

# API-4 (Fetch if the elevator is moving up or down currently)
    @action(detail=True, methods=['get'])
    def get_elevator_current_direction(self, request, elevator_id):
        try:
            elevator = Elevator.objects.get(elevator_id=elevator_id)
        except Exception as e:
            return Response({'message': 'Elevator does not exist'})
        current_direction = elevator.direction
        return Response({'elevator_direction': current_direction})

# API-5 (Mark a elevator as not working or in maintenance)
    @action(detail=True, methods=['put'])
    def update_elevator_under_maintenance_status(self, request, elevator_id):
        try:
            elevator = Elevator.objects.get(elevator_id=elevator_id)
        except Exception as e:
            return Response({'message': 'Elevator does not exist'})
        elevator.status = "Under_Maintenance"
        elevator.save()
        return Response({"elevator_status": elevator.status})

# API-6 (Open/close the door.)
    @action(detail=True, methods=['put'])
    def update_elevator_open_or_close_door(self, request, elevator_id):
        try:
            elevator = Elevator.objects.get(elevator_id=elevator_id)
        except Exception as e:
            return Response({'message': 'Elevator does not exist'})
        elevator.doors_open = False
        elevator.save()
        return Response({"open_close_door": elevator.doors_open})


class ElevatorRequestViewSet(viewsets.ModelViewSet):
    queryset = ElevatorRequest.objects.all()
    serializer_class = ElevatorRequestSerializer

# API-7 (Saves user request to the list of requests for a elevator)
    @action(detail=True, methods=['post'])
    def create_user_elevator_request(self, request, elevator_id):
        try:
            elevator = Elevator.objects.get(elevator_id=elevator_id)
        except Elevator.DoesNotExist:
            return Response({'message': 'Elevator does not exist'})

        floor = request.data.get('floor')
        if floor is None:
            return Response({'message': 'Floor value is required'}, status=400)

        data = {'elevator': elevator.pk, 'floor': floor}
        serializer = ElevatorRequestSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

