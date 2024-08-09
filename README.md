# Airfare-Prediction-using-Random-Forest-Regressor

This is a Django-based project for predicting airfare prices. The project is structured as a standard Django application.
The project used Random forest regression algorithm to predict the price based on the user entered details obtained from the input form from the home page.


## Project Structure

Airfare_Prediction/
├── Airfare_Prediction/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── __pycache__/
│   │   └── [compiled Python files]
├── Customer/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│       └── __init__.py
├── templates/
│   └── home.html
├── db.sqlite3
└── manage.py


## Setup Instructions

 ### Prerequisites

 - Python 3.x
 - Django 3.x
 - SQLite (comes pre-installed with Python)

### Installation

 1. **Clone the repository**:
    ```bash
    git clone https://github.com/Riyaz-021/Airfare-Prediction-using-Random-Forest-Regressor.git  


 2. **Install the Dependencies**:
    Make sure you have Django installed. You can install it using pip.

    ```bash
    pip install django


 3. **Run the migrations**:
    Apply the migrations to set up the database schema:

    ```bash
    python manage.py migrate


 4. **Run the model.py file (first time only)**:
    This is to initialise the model:

    ```bash
    python model.py


 5. **Run the server**:
    Start the development server:

    ```bash
    python manage.py runserver


## License

This project is licensed under the MIT License - see the LICENSE file for details.

