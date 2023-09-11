from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth import login as auth_login, authenticate, logout
# Create your views here.

def index(request):
    return render(request, "mover/index.html", {})

def component(request):
    return render(request, "mover/component.html", {})

def accept_request(request):
    return render(request, "mover/driver_pages/accept_request.html", {})

def ready_to_move(request):
    return render(request, "mover/driver_pages/ready_to_move.html", {})

def request_mover(request):
    return render(request, "mover/request_mover.html", {})

def mover_details(request):
    return render(request, "mover/mover_details.html", {})

def driver_onboarding(request):
    return render(request, "mover/driver_onboarding.html", {})


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("/")
    
    form = CustomUserCreationForm()
    
    return render(request, "registration/signup.html", {"form": form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            email = request.POST["email"]
            password = request.POST["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                user = form.get_user()
                auth_login(request, user)
                return redirect('/')  # Redirect to a success page
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("/")
    
    
    