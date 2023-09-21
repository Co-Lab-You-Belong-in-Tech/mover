from django.urls import path
from .views import (document_verification, login, logout_view,
                    index, accept_request, select_mover, signup, application_status,
                    ready_to_move, vehicle_information,
                    ready_to_move_customer, before_moving, send_email)

urlpatterns = [
    path('', index, name="index"),
    path('select-mover/<str:tracking_id>/', select_mover, name="select_mover"),
    path('accept-request/', accept_request, name="accept_request"),
    path('before-moving/<str:tracking_id>/',
         before_moving, name="before_moving"),
    path('ready-to-move/',
         ready_to_move, name="ready_to_move"),
    path('ready-to-move/customer/<int:pk>/<str:tracking_id>/', ready_to_move_customer,
         name="ready_to_move_customer"),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("logout_view/", logout_view, name="logout_view"),
    path("document/verification", document_verification,
         name="document_verification"),
    path("vehicle/information", vehicle_information, name="vehicle_information"),
    path("application/status", application_status, name="application_status"),
    path('send-email/', send_email, name="send_email"),
]
