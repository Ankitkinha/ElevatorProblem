from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory

from elevator_app.models import Elevator, ElevatorRequest
from elevator_app.serializers import ElevatorRequestSerializer
from elevator_app.views import ElevatorViewSet


class ElevatorViewSetTestCase(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = ElevatorViewSet.as_view({'get': 'get_elevator_requests'})
        self.elevator = Elevator.objects.create(elevator_id=1, current_floor=1)
        self.url = reverse('elevator-requests-detail', args=[self.elevator.pk])

    def test_get_elevator_requests(self):
        # Create some elevator requests
        request1 = ElevatorRequest.objects.create(elevator=self.elevator, floor=10)
        request2 = ElevatorRequest.objects.create(elevator=self.elevator, floor=20)

        # Create a GET request
        request = self.factory.get(self.url)

        # Call the view
        response = self.view(request, pk=self.elevator.pk)

        # Verify the response
        self.assertEqual(response.status_code, 200)

        # Verify the response data
        expected_data = ElevatorRequestSerializer(
            [request1, request2], many=True, context={'request': request}
        ).data
        self.assertEqual(response.data, expected_data)
