from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from elevator_app.models import Elevator
from elevator_app.views import ElevatorViewSet


class ElevatorViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ElevatorViewSet.as_view({'get': 'get_elevator_next_destination_floor'})
        self.elevator = Elevator.objects.create(elevator_id=1, current_floor=0)
        self.url = reverse('elevator-next-floor', args=[self.elevator.pk])

    def test_get_elevator_next_destination_floor(self):
        # Create a GET request
        request = self.factory.get(self.url)

        # Call the view
        response = self.view(request, elevator_id=self.elevator.pk)

        # Verify the response
        self.assertEqual(response.status_code, 200)

        # Verify the response data
        next_floor = self.elevator.current_floor + 1
        expected_data = {'next_destination_floor': next_floor}
        self.assertEqual(response.data, expected_data)
