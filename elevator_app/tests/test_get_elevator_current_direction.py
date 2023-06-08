from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from elevator_app.models import Elevator
from elevator_app.views import ElevatorViewSet


class ElevatorViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ElevatorViewSet.as_view({'get': 'get_elevator_current_direction'})
        self.elevator = Elevator.objects.create(elevator_id=1, direction='Upward', current_floor=1)
        self.url = reverse('elevator-direction', args=[self.elevator.pk])

    def test_get_elevator_current_direction(self):
        # Create a GET request
        request = self.factory.get(self.url)

        # Call the view
        response = self.view(request, elevator_id=self.elevator.pk)

        # Verify the response
        self.assertEqual(response.status_code, 200)

        # Verify the response data
        expected_data = {'direction': self.elevator.direction}
        self.assertEqual(response.data, expected_data)
