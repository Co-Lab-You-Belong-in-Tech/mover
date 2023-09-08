from django.urls import path
from .views import component, driver_onboarding, index, accept_request, mover_details, request_mover

urlpatterns = [
    path('', index, name = "index"),
    path('component/', component, name = "component"),
    path('accept-request/', accept_request, name = "accept_request"),
    path('request-mover/', request_mover, name = "request_mover"),
    path('mover-details/', mover_details, name = "mover_details"),
    path('driver-onboarding/', driver_onboarding, name = "driver_onboarding"),
]
