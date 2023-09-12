from django.shortcuts import redirect, render
from .forms import CustomAuthenticationForm, CustomUserCreationForm, DocumentVerificationForm, VehicleInformationForm
from django.contrib.auth import login as auth_login, authenticate, logout
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, "mover/landing_page.html", {})

def mapview(request):
    return render(request, "mover/components/map.html", {})

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
        form = CustomUserCreationForm(request.POST, request.FILES)
        print(f"file: {request.FILES} post data: {request.POST}")
        if form.is_valid():
            user = form.save()
            print("valid user: ", user)
            auth_login(request, user)
            print("Redirecting to homepage")
            # Move to the next step of vehicle verification
            return redirect(reverse("document_verification"))
    
    form = CustomUserCreationForm()
    
    return render(request, "mover/driver_pages/create_account.html", {"form": form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request.POST)
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
    
def document_verification(request):
    if request.method == "POST":
        print(f"file: {request.FILES} post data: {request.POST}")
        print("Current user: ", request.user)
        form = DocumentVerificationForm(request.POST, request.FILES, instance = request.user)
        print(f"Form valid: {form.is_valid}")
        
        if form.is_valid():
            print("Updated the db!!")
            form.save()
            return redirect(reverse("vehicle_information"))
    
    form = DocumentVerificationForm()
    return render(request, "mover/driver_pages/document_verification.html", {"form": form})
    
def vehicle_information(request):
    
    if request.method == "POST":
        print(f"file: {request.FILES} post data: {request.POST}")
        print("Current user: ", request.user)
        form = VehicleInformationForm(request.POST, request.FILES)
        
        print(f"Form valid: {form.is_valid}")
        
        if form.is_valid():
            # update the form model instance to be the current logged in user
            form.instance.driver = request.user
            form.save()
            print(f"Updated the db!! Driver: {form.instance.driver}")
            
            return redirect(reverse("application_status"))
    
    form = VehicleInformationForm()
    return render(request, "mover/driver_pages/vehicle_information.html", {"form": form})
    
def application_status(request):
    return render(request, "mover/driver_pages/application_status.html")