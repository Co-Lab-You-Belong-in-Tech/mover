from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render

from .forms import (BookingUpdateForm, CustomAuthenticationForm, CustomUserCreationForm, BookingForm,
                    DocumentVerificationForm, VehicleInformationForm)
from django.contrib.auth import login as auth_login, authenticate, logout
from django.urls import reverse
from .models import CustomUser, Vehicle, Booking
import uuid
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .utils import custom_send_mail
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Create your views here.

HOST_EMAIL = os.getenv("EMAIL_HOST_USER")


def index(request):
    """For anonyomous user once they land on the root url, set a cookie of unique id.
    This will allow to track all the bookings that they make.
    """

    if request.user.is_authenticated:
        print(request.user.is_authenticated)
        return redirect("accept_request")

    form = BookingForm()

    tracking_id = str(uuid.uuid4())

    if request.method == "POST":
        form = BookingForm(request.POST, request.FILES)

        if form.is_valid():

            booking = form.save(commit=False)
            booking.tracking_id = tracking_id
            form.save()

            return redirect("before_moving", tracking_id=tracking_id)

    return render(request, "mover/landing_page.html", {"form": form, "tracking_id": tracking_id})


def before_moving(request, tracking_id):
    """
    This handles the customer before moving page 2. Where the items details and note to driver is
    entered
    """
    form = BookingUpdateForm()

    booking_instance = get_object_or_404(Booking, tracking_id=tracking_id)
    print(booking_instance)

    if request.method == "POST":
        form = BookingUpdateForm(
            request.POST, request.FILES, instance=booking_instance)

        if form.is_valid():
            print("form is valid")
            form.save()
            return redirect("select_mover", tracking_id=tracking_id)
    context = {
        "form": form
    }
    return render(request, "mover/customer_pages/before_moving.html", context)


def select_mover(request, tracking_id):
    """
        This gets all drivers and list for the customer so they can select one to move with.
    """
    # Get a list of all the vehicles that are currently set to available
    # available_vehicles = get_list_or_404(Vehicle, is_available=True)
    available_vehicles = Vehicle.objects.filter(is_available=True)

    context = {
        'available_vehicles': available_vehicles,
        "tracking_id": tracking_id
    }
    return render(request, "mover/customer_pages/select_mover.html", context)


def ready_to_move_customer(request, pk, tracking_id):
    """Get a the mover vehicle that was passed in and then query the db for it. After the customer
    selects a mover an email is sent to the both the driver and customer. This will serve as a notification
    for the driver to accept the request."""

    vehicle = get_object_or_404(Vehicle, pk=pk)
    booking = get_object_or_404(Booking, tracking_id=tracking_id)
    booking_email = booking.email
    # Send email of success to the user.
    # email_context = {
    #     "pickup": booking.pickup_location,
    #     "dropoff": booking.dropoff_location,
    #     "driver": vehicle.driver.get_full_name(),
    # }
    # email_html = render_to_string(
    #     "mover/emails/email_template_customer.html", email_context)

    # subject = 'Hello, You have Successfully Booked A Service'
    # from_email = os.getenv("EMAIL_HOST_USER")
    # recipient_list = [booking_email]  # Recipient's email address
    # message = "Booked A Service!"

    # send_mail(subject, message, from_email,
    #           recipient_list, html_message=email_html)

    # print("Sent mail to customer")

    # # Send email to driver
    # email_context_driver = {
    #     "pickup": booking.pickup_location,
    #     "dropoff": booking.dropoff_location,
    #     "customer_email": booking_email,
    # }
    # email_html_driver = render_to_string(
    #     "mover/emails/email_template_driver.html", email_context_driver)

    # subject = 'Hello, You have a customer request!!'

    # from_email = os.getenv("EMAIL_HOST_USER")
    # recipient_list = [vehicle.driver.email]  # Recipient's email address
    # message = "Someone Booked A Service!"

    # send_mail(subject, message, from_email,
    #           recipient_list, html_message=email_html_driver)
    # print("Sent mail to driver")

    context = {
        "tracking_id": tracking_id,
        "pk": pk,
        "vehicle": vehicle,
        "booking": booking,
    }
    return render(request, "mover/customer_pages/ready_to_move.html", context)


def send_email(request):
    email_context = {
        "pickup": "Utah",
        "dropoff": "San Jose",
        "driver": "Sixtus",
    }
    email_html_driver = render_to_string(
        "mover/emails/email_template_customer.html", email_context)

    subject = 'Again Hello, You have Successfully Booked A Service'
    message = "You just Booked A Service!!"
    from_email = "sparkdkiller@gmail.com"
    recipient_list = ["sikky606@gmail.com",]

    send_mail(subject, message, from_email,
              recipient_list)
    # if is_sent:
    #     return HttpResponse("Sent Email")

    return HttpResponse("Email sent...")


def accept_request(request):
    """Get all current orders with no drivers yet and present to the driver"""

    bookings = Booking.objects.filter(owner=None)
    # Check if current user has unfufuilled requests
    query = Booking.objects.filter(is_fufuilled=False, owner=request.user)

    context = {
        "bookings": bookings,
        "can_accept_request": True
    }
    # Add a context of false to avoid accepting multiple unfuifuiled orders
    if query:
        context["can_accept_request"] = False
        context["unfufuilled_booking"] = query

    return render(request, "mover/driver_pages/accept_request.html", context)


def ready_to_move(request):
    """This handles when the driver accepts a request that a customer chose thier vehicle for.
    Once they accept, a text will be sent to the user that they have accepted."""
    if request.method == "POST":
        tracking_id = request.POST.get("tracking_id")

        booking = get_object_or_404(Booking, tracking_id=tracking_id)

        booking.owner = request.user
        booking.save()
        context = {
            "booking": booking
        }
        # Send another email to both the customer and the driver, saying the driver accepted the request.
        return render(request, "mover/driver_pages/ready_to_move.html", context)

    return reverse("accept_request")


def list_fulfilled_requests(request):
    """
        Get all the fulfilled orders for that particular driver and display. Serves as a history.
    """
    fulfilled_bookings = Booking.objects.filter(
        owner=request.user, is_fufuilled=True)

    context = {
        "fulfilled_bookings": fulfilled_bookings
    }
    return render(request, "mover/driver_pages/fulfilled_requests.html", context)


def fulfill_request(request, id):
    """
        This is will get the booking of given id and set it to fulfilled then redirect the user to
        list fulfilled requests view.
    """
    if request.method == "POST":
        booking = get_object_or_404(Booking, id=id)
        booking.is_fufuilled = True
        booking.save()

    return redirect("list_fulfilled_requests")


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
            return redirect("document_verification")

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
        form = DocumentVerificationForm(
            request.POST, request.FILES, instance=request.user)
        print(f"Form valid: Not yet")

        if form.is_valid():
            print("Updated the db!!")
            form.save()
            return redirect("vehicle_information")

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

            return redirect("application_status")

    form = VehicleInformationForm()
    return render(request, "mover/driver_pages/vehicle_information.html", {"form": form})


def application_status(request):
    return render(request, "mover/driver_pages/application_status.html")
