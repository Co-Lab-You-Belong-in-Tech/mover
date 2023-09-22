from django.core.mail import send_mail
from django.template.loader import render_to_string
import os
from dotenv import load_dotenv

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
