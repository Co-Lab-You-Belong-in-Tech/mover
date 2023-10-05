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


def get_driving_data2(origin: str, destination: str) -> str:
    """
        This will take two cordinates(pickup_location, driver_location) then gets the driving time taken
        for a driver to go from their current location to the pick up location.
        Args:
            origin(str): the pickup latitude and longitude seperated with ","
            destination(str): the driver latitude and longitude seperated with ","
        Returns: 
            list: (distance, duration)
        Examples:
            origin = "47.6044,-122.3345"
            destination = "45.5347,-122.6231"
    """
    url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix"

    # origin = "47.6044,-122.3345"
    # destination = "45.5347,-122.6231"

    # Define the query parameters as a dictionary
    params = {
        "origins": origin,
        "destinations": destination,
        "travelMode": "driving",
        "distanceUnit": "mi",
        "key": os.getenv("BING_KEY"),
    }
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
        print("Distance:", distance, duration)
        return (distance, duration)
    else:
        print(f"Request failed with status code {response.status_code}")
        return False


def get_driving_data(origin1: str, origin2: str, destination1: str, destination2: str):
    """
        Gets the travel distance it takes to go from one point(long, lat) to a destination(lat, long)
        origin: "47.6044,-122.3345"
        destination: "45.5347,-122.6231"
        returns: (distance, duration) in miles and minutes
    """

    url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix"

    # Define the query parameters as a dictionary

    origin = f"{origin1},{origin2}"
    destination = f"{destination1},{destination2}"
    # origin = "47.6044,-122.3345"
    # destination = "45.5347,-122.6231"

    params = {
        "origins": origin,
        "destinations": destination,
        "travelMode": "driving",
        "distanceUnit": "mi",
        "key": os.getenv("BING_KEY"),
    }
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
        print("Distance:", distance, duration)
        return (distance, duration)
    else:
        print(f"Request failed with status code {response.status_code}")
        return False


def get_lat_long(address: str):
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
                    # print(f"Address: {address}")
                    # print(f"Longitude: {longitude}")
                    # print(f"Latitude: {latitude}")
                    return (latitude, longitude)
        else:
            print(f"Request failed with status code {response.status_code}")

    except Exception as e:
        print(e)


# origin1 = get_lat_long("Texas")
# origin2 = get_long_lat("Texas")

# print(f"Texas({origin1})")

# Hollywood((-118.32950592, 34.09798813)) Texas((-99.33329773, 31.46384811))

# (distance, duration) = get_driving_data(
#     "34.09798813", "-118.32950592", "31.46384811", "-99.33329773")

# print(f"Distance({distance} miles) Duration({duration} mintues)")
