from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_email(subject, message, from_email, recipient_list, html_email):
    try:
        # email_context = {
        #     "pickup": "Utah",
        #     "dropoff": "San Jose",
        #     "driver": "Sixtus",
        # }
        # email_html = render_to_string(
        #     "mover/emails/email_template.html", email_context)

        # subject = 'HTML Email Example'
        # message = 'This is a plain text email message.'
        # # Sender's email (should match EMAIL_HOST_USER)
        # from_email = 'sparkdkiller@gmail.com'
        # recipient_list = ['sikky606@gmail.com']  # Recipient's email address

        # # Send the email with the HTML content
        send_mail(subject, message, from_email,
                  recipient_list, html_message=html_email)
        return True
    except:
        print("Error sending mail...")
        return False
