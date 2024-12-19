# Ad-reimbursement
## Technologies
- Python 3.9
- Django 5.0

## Running Locally

### Requirements

- Python version 3.9.6 (use [virtualenv](https://docs.python.org/3/library/venv.html) to manage your Python versions)


### First Time Setup

1. Clone repo and cd into directory
1. Create virtual environment: `python -m venv venv` (you could also use Poetry for this step, but I think it's easier this way)
1. Run: `source venv/bin/activate`
1. Run migrations: `python manage.py migrate ad_api`
1. Create an admin user for logging into the Django admin interface: `python manage.py createsuperuser`


### Running the App

1. Make sure you are already in your virtual environment: `source venv/bin/activate`
1. Run the app: `python manage.py runserver`
1. View the API at http://localhost:8000 and the admin interface at http://localhost:8000/admin
