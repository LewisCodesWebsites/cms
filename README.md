# Simple CMS

This repository contains a minimal Content Management System built with **Django**. It supports:

- User registration and authentication
- Creating and editing content items
- Basic versioning for each piece of content
- Listing your content items

## Requirements

- Python 3.12+
- pip

## Setup

Install dependencies and run the development server:

```bash
pip install django==5.0.2
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

You can create a superuser to access the Django admin:

```bash
python manage.py createsuperuser
```

After starting the server, visit `http://localhost:8000/` to register a new user, create content, and view your content items.
