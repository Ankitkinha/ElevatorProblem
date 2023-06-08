from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from elevator_app.models import Elevator
from elevator_app.views import ElevatorViewSet


class ElevatorViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ElevatorViewSet.as_view({'put': 'update_elevator_under_maintenance_status'})
        self.elevator = Elevator.objects.create(elevator_id=1, status='under_maintenance', current_floor=1)
        self.url = reverse('under-maintenance', args=[self.elevator.pk])

    def test_update_elevator_under_maintenance_status(self):
        # Create a PUT request
        request = self.factory.put(self.url)

        # Call the view
        response = self.view(request, elevator_id=self.elevator.pk)

        # Verify the response
        self.assertEqual(response.status_code, 200)

        # Verify the response data
        self.elevator.refresh_from_db()
        expected_data = {"under_maintenance": self.elevator.status}
        self.assertEqual(response.data, expected_data)
        self.assertEqual(self.elevator.status, "Under_Maintenance")
