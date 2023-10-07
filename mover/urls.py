from django.urls import path
from .views import (document_verification, login, logout_view, fulfill_request,
                    request_mover, accept_request, select_mover, signup, application_status,
                    ready_to_move, vehicle_information, list_fulfilled_requests,
                    ready_to_move_customer, before_moving, send_email, home)

urlpatterns = [
    path('', home, name="home"),
    path('request-mover', request_mover, name="request_mover"),
    path('select-mover/<str:tracking_id>/', select_mover, name="select_mover"),
    path('accept-request/', accept_request, name="accept_request"),
    path('before-moving/<str:tracking_id>/',
         before_moving, name="before_moving"),
    path('ready-to-move/',
         ready_to_move, name="ready_to_move"),
    path('ready-to-move/customer/<int:pk>/<str:tracking_id>/', ready_to_move_customer,
         name="ready_to_move_customer"),
    path("fulfilled-requests/", list_fulfilled_requests,
         name="list_fulfilled_requests"),
    path("fulfill-request/<int:id>/", fulfill_request, name="fulfill_request"),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("logout_view/", logout_view, name="logout_view"),
    path("document/verification", document_verification,
         name="document_verification"),
    path("vehicle/information", vehicle_information, name="vehicle_information"),
    path("application/status", application_status, name="application_status"),
    path('send-email/', send_email, name="send_email"),
]
