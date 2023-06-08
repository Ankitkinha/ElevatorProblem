from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from elevator_app.models import Elevator


class CreateUserElevatorRequestTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.elevator = Elevator.objects.create(elevator_id=1, current_floor=5)
        self.url = f'/elevators/{self.elevator.pk}/userrequest/'

    def test_create_user_elevator_request(self):
        elevator = self.elevator.pk
        floor = 5
        data = {'elevator': elevator, 'floor': floor}

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        request_data = response.json()
        self.assertEqual(request_data['elevator'], self.elevator.pk)
        self.assertEqual(request_data['floor'], floor)

    def test_create_user_elevator_request_missing_floor(self):
        data = {}  # Missing 'floor' field

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
