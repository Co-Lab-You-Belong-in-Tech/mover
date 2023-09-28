from django.core.mail import send_mail
from django.template.loader import render_to_string
import os
from dotenv import load_dotenv
import requests

load_dotenv()


def custom_send_mail(email_context: dict, recipient_list: list, email_type) -> bool:
    """
        Send mail using the template in email.
    """
    try:
        from_email = os.getenv("EMAIL_HOST_USER")

        if email_type.lower() == "driver":

            email_html_driver = render_to_string(
                "mover/emails/email_template_driver.html", email_context)

            subject = 'Hello, You have a customer request!!'
            message = "Someone Booked A Service!"

            send_mail(subject, message, from_email,
                      recipient_list, html_message=email_html_driver)

            return True

        elif email_type.lower() == "customer":

            email_html_customer = render_to_string(
                "mover/emails/email_template_customer.html", email_context)

            subject = 'Hello, You have Successfully Booked A Service'
            message = "You just Booked A Service!!"

            print(subject, message, from_email,
                  recipient_list, email_html_customer)

            send_mail(subject, message, from_email,
                      recipient_list, html_message=email_html_customer)

            return True

        elif email_type.lower() == "driver_accept":

            email_html_driver_accept = render_to_string(
                "mover/emails/driver_accept.html", email_context)

            subject = 'Hello, Your Driver is On The Way'
            message = "Driver accepted your request!!"

            send_mail(subject, message, from_email,
                      recipient_list, html_message=email_html_driver_accept)

            return True

        else:
            return False

    except Exception as e:
        print("Error sending mail...", e)
        return False


def get_driving_data(origin1: str, origin2: str, destination1: str, destination2: str):
    """
        Gets the travel distance it takes to go from one point(long, lat) to a destination(long, lat)
        origin: "47.6044,-122.3345"
        destination: "45.5347,-122.6231"
        returns: (distance, duration)
    """

    url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix"

    # Define the query parameters as a dictionary

    origin = origin1 + "," + origin2
    destination = destination1 + "," + destination2

    params = {
        "origins": origin,
        "destinations": destination,
        "travelMode": "driving",
        "key": os.getenv("BING_KEY"),
    }
    print(params)
    # Make the GET request
    response = requests.get(url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Extract and print the distances and durations
        results = data["resourceSets"][0]["resources"][0]["results"]
        distance = results[0]['travelDistance']
        duration = results[0]['travelDuration']

        return (distance, duration)
    else:
        print(f"Request failed with status code {response.status_code}")
        return False


def get_long_lang(address: str):
    """
    This returns the long and lat of a single address.
    address = "6322 Fauntleroy Way SW Seattle"
    """
    try:
        base_url = "https://dev.virtualearth.net/REST/v1/Locations"

        # Define the query parameters
        params = {
            "q": address,
            "key": os.getenv("BING_KEY")
        }

        # Make the GET request to the Geocoding API
        response = requests.get(base_url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Extract the latitude and longitude from the response
            if "resourceSets" in data and len(data["resourceSets"]) > 0:
                resources = data["resourceSets"][0]["resources"]
                if len(resources) > 0:
                    coordinates = resources[0]["point"]["coordinates"]
                    latitude, longitude = coordinates
                    print(f"Address: {address}")
                    print(f"Latitude: {latitude}")
                    print(f"Longitude: {longitude}")
                    return (longitude, latitude)
        else:
            print(f"Request failed with status code {response.status_code}")

    except Exception as e:
        print(e)
