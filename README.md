# Aircraft Logger App

![ [alt_image](url_image_shields_io) ](https://img.shields.io/badge/python-3.8.6-blue)
![ [alt_image](url_image_shields_io) ](https://img.shields.io/badge/django-3.1.4-green)
![ [alt_image](url_image_shields_io) ](https://img.shields.io/badge/django--rest--framework-3.12.2-red)

This API allows registering data of flight, aircraft and airport easily.
Is developed in DjangoRestFramework plus third-party libraries such as pandas, drf-yasg and django-filters.

## Features

- CRUD operations for those three entities by using the endpoints.
- Filter flights by arrival and departure airports and datetime.
- Report of flights (with in-time-flight average per flight) by airport and also filterable by datetime.

## Installation

- Clone this repo: `git clone git@github.com:carlosjimz87/aircraftlogger.git && cd aircraftlogger`
- Activate a virtualenv: `virtualenv env && source env/bin/activate`
- Install dependencies: `pip install -r requirements.txt`
- Create database: `python manage.py migrate`

## Testing

- Run all tests: `python manage.py test`

## Usage

- Populate database with dummy data : `python manage.py populate`
- Run server on local: `python manage.py runserver`
- Open homepage in a browser at http://localhost:8000/
- Open swagger in a browser at http://localhost:8000/swagger/
