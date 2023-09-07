from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "mover/index.html", {})

def component(request):
    return render(request, "mover/component.html", {})

def accept_request(request):
    return render(request, "mover/accept_request.html", {})

def request_mover(request):
    return render(request, "mover/request_mover.html", {})

def mover_details(request):
    return render(request, "mover/mover_details.html", {})