from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from elevator_app.models import Elevator
from elevator_app.views import ElevatorViewSet


class ElevatorViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ElevatorViewSet.as_view({'put': 'update_elevator_open_or_close_door'})
        self.elevator = Elevator.objects.create(elevator_id=1, doors_open=True, current_floor=1)
        self.url = reverse('open-close-door', args=[self.elevator.pk])

    def test_update_elevator_open_or_close_door(self):
        # Create a PUT request
        request = self.factory.put(self.url)

        # Call the view
        response = self.view(request, elevator_id=self.elevator.pk)

        # Verify the response
        self.assertEqual(response.status_code, 200)

        # Verify the response data
        self.elevator.refresh_from_db()
        expected_data = {"open_close_door": self.elevator.doors_open}
        self.assertEqual(response.data, expected_data)
        self.assertEqual(self.elevator.doors_open, False)
