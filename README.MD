### Mover

An app that connects people with local vehicle movers!

### How to set up

- Set up a virtual envrionment using pipenv or virtualenv
- if you don't have pipenv, run `pip install pipenv`
- Now clone the repo `git clone https://github.com/Co-Lab-You-Belong-in-Tech/mover`
- Run the following command to install the packages listed in requirements.txt file: `pipenv install requirements.txt`
- Make sure you are in the root directory and run: `python manage.py makemigrations`
- Next run: `python manage.py migrate`
- Finally, run `python manage.py runserver`
- Go to "http://127.0.0.1:8000/" to view the app.

### Authentication

Below are routes to the user auth:
- Login: http://127.0.0.1:8000/accounts/login/
- Sign up: http://127.0.0.1:8000/accounts/signup/

### TODO Production
- Debug Microsoft Map not showing [DONE]
- Set up file upload (MEDIA ROOT)
- Redeploy to moveritems.pythonanywhere.com and confirm everything is working. [IMPORTANT]


### TODO DEV
- Debug email not sending [IMPORTANT]
- Only authenticated users should be able to see the document verification and document upload views [IMPORTANT][DONE]
- Handle Cancel Trip on the ready to move screen. This should remove the vehicle from booking and set the
vehicle availablity to True. So it can shown on the select mover screen again.
- Fix the per hour issue on the move screen
- Debug user selecting a mover and acept a request conflict [IMPORTANT][DONE]
- Create/ReFactor the Customer Request A Mover Screen[IMPORTANT][DONE]
- Create Driver Log In Screen [DONE]
- Create Driver Onboarding Screen [DONE]
- Create Request a mover screen [DONE]
- Create before you get moving screen [DONE]
- Link the Navbar Login, Sign Up, Find a driver to their respective views [DONE]
- Create select a mover screen [DONE]
- Create get ready to move screen for mover [DONE]
- Make the login page work. [DONE]
- Make the driver sign up page work [DONE]
- Add a view to toggle fufuilled is the driver confirms it. [DONE]
- Add a sreen to show all of a driver's fufuilled orders history. [DONE]
- Add filter functionality to the select mover page.
- Send an email to driver and customer after accepting a request withe the booking details [DONE]
- Add JS to save pick up and drop off location to localstorage and persist it in map. [DONE]
- Add form errors to all forms so users can know what th
ey did wrong.
- Enable messages to show notifications on the front end:
- Style the email templates to be better
- Add placeholders to the input in customer and driver pages.
- Fix the fulfuilled typos both in the model and template. [FUTURE]
- Driver Dashboard to update their contact details [FUTURE]
- If authenticated the location of the map should be cleared.

## TODO DEV DEBUG
- Fix Driver Accept Request CSS making map not to appear [DONE]
- Fix Styling of Radio Buttons for Customer side [DONE]
