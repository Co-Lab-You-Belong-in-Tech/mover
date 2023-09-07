from django.urls import path
from .views import component, index, accept_request

urlpatterns = [
    path('', index, name = "index"),
    path('component/', component, name = "component"),
    path('accept-request/', accept_request, name = "accept_request")
]
