# Lab 26: Intro to Django

## Overview

Build out a small, but functional, multi page web site using Django.

## Feature Tasks

Create web site in Django with 2 pages

- home page
- about page
- create views/urls/templates as needed for home and about pages
- use ancestor template to contain navigation elements
- Should be built the “Django way” aka match the structure of in-class demo

### Setup

1. Create a virtual environment --> python –m venv .venv
2. Activate the virtual environment --> source .venv/bin/activate (for Linux and MacOS); .\.venv\Scripts\activate (for Windows)
3. Install Django --> pip install django
4. Create and start a Django project --> django-admin startproject djangho_snack_tracker_project .
5. Set up migrations --> python manage.py migrate
6. Run development server --> python manage.py runserver
7. Create a Django app --> python manage.py startapp snacks
8. Need to complete 3 steps before making migrations: TUV --> (1) templates (folder with base.html), (2) urls (in snacks folder), and (3) views(in snacks folder)
9. Make and apply migrations --> python manage.py makemigrations snacks
10. Apply the migrations --> python manage.py runserver
11. Create a super user as the administator of the site --> python manage.py createsuperuser

- username: admin
- email address: admin@admin.com
- password: admin

12.Test that the TUV and migrations worked in the development server
13.Add /admin to the end of the local host url to log in with the admin credentials

### Tests

python manage.py test
