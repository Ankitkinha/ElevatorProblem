from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from elevator_app.models import Elevator
from elevator_app.views import ElevatorViewSet


class ElevatorViewSetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.view = ElevatorViewSet.as_view({'post': 'initialize_elevator_system'})
        self.url = '/elevators/initializesystem'

    def test_initialize_elevator_system(self):
        # Set the number of elevators to initialize
        num_elevators = 3

        # Send a POST request with the number of elevators in the data
        response = self.client.post(self.url, data={'num_elevators': num_elevators}, format='json')

        # Verify the response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Verify the response data
        elevators = Elevator.objects.all()
        self.assertEqual(len(elevators), num_elevators)
        for elevator_data, elevator in zip(response.data, elevators):
            self.assertEqual(elevator_data['elevator_id'], elevator.elevator_id)

        # Clean up the created elevators
        Elevator.objects.all().delete()
