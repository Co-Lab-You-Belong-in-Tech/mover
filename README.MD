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
- Set up file upload (NEDIA ROOT)

### TODO DEV
- Create/ReFactor the Customer Request A Mover Screen[IMPORTANT]
- Create Driver Log In Screen [DONE]
- Create Driver Onboarding Screen [DONE]
- Create Request a mover screen [DONE]
- Create before you get going screen
- Create select a mover screen
- Link the Navbar Login, Sign Up, Find a driver to their respective views
- Make the login page work.
- Make the driver sign up page work