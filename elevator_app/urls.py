from django.urls import path, include
from rest_framework import routers

from elevator_app.views import ElevatorRequestViewSet, ElevatorViewSet

router = routers.DefaultRouter()
router.register(r'elevators', ElevatorViewSet, basename='elevator')
router.register(r'elevators/<int:elevator_id>/get_elevator_requests', ElevatorRequestViewSet,
                basename='elevator-requests')

urlpatterns = [
    path('', include(router.urls)),
    path('elevators/initializesystem', ElevatorViewSet.as_view(
        {'post': 'initialize_elevator_system'}), name='initialize-system'),
    path('elevators/<int:elevator_id>/nextfloor/', ElevatorViewSet.as_view(
             {'get': 'get_elevator_next_destination_floor'}), name='elevator-next-floor'),
    path('elevators/<int:elevator_id>/elevatorcurrentdirection/', ElevatorViewSet.as_view(
        {'get': 'get_elevator_current_direction'}), name='elevator-direction'),
    path('elevators/<int:elevator_id>/undermaintenance/', ElevatorViewSet.as_view(
        {'put': 'update_elevator_under_maintenance_status'}), name='under-maintenance'),
    path('elevators/<int:elevator_id>/openclosedoor/', ElevatorViewSet.as_view(
        {'put': 'update_elevator_open_or_close_door'}), name='open-close-door'),
    path('elevators/<int:elevator_id>/userrequest/', ElevatorRequestViewSet.as_view(
        {'post': 'create_user_elevator_request'}), name='user-request')
]
