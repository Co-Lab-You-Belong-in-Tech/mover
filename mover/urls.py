from django.urls import path
from .views import (component, document_verification, driver_onboarding, login, logout_view,
                    index, accept_request, signup, application_status, mapview,
                    mover_details, ready_to_move, request_mover, vehicle_information)

urlpatterns = [
    path('', index, name = "index"),
    path('component/', component, name = "component"),
    path('mapview/', mapview, name = "mapview"),
    path('accept-request/', accept_request, name = "accept_request"),
    path('request-mover/', request_mover, name = "request_mover"),
    path('ready-to-move/', ready_to_move, name = "ready_to_move"),
    path('mover-details/', mover_details, name = "mover_details"),
    path('driver-onboarding/', driver_onboarding, name = "driver_onboarding"),
    path("signup/", signup, name = "signup"),
    path("login/", login, name = "login"),
    path("logout_view/", logout_view, name = "logout_view"),
    path("document/verification", document_verification, name = "document_verification"),
    path("vehicle/information", vehicle_information, name = "vehicle_information"),
    path("application/status", application_status, name = "application_status"),
]
