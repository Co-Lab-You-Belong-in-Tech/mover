from django.urls import path
from .views import (component, driver_onboarding, login, logout_view,
                    index, accept_request, signup, 
                    mover_details, ready_to_move, request_mover)

urlpatterns = [
    path('', index, name = "index"),
    path('component/', component, name = "component"),
    path('accept-request/', accept_request, name = "accept_request"),
    path('request-mover/', request_mover, name = "request_mover"),
    path('ready-to-move/', ready_to_move, name = "ready_to_move"),
    path('mover-details/', mover_details, name = "mover_details"),
    path('driver-onboarding/', driver_onboarding, name = "driver_onboarding"),
    path("signup/", signup, name = "signup"),
    path("login/", login, name = "login"),
    path("logout_view/", logout_view, name = "logout_view"),
]
