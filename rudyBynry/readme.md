## Tasklist

- Setup and Configuration
 * [x] Create Django project
 * [ ] Set up virtual environment
 * [x] note down commndas used
 * [x] Set up database (SQLite for development)

- User Authentication (accounts app)
 * [x] Create CustomUser model
 * [x] Implement user registration
 * [x] Implement user login
 * [ ] Implement user logout

- Service Requests (service_requests app)
 * [x] Create ServiceRequest model
 * [x] service request submission
 * [x] service request list view
 * [x] service request detail view
 * [ ] service request update 
 * [ ] file attachment 

 * [ ] Make better UI
 * [ ] documentation
 

# Bynry Intern Assignment


## Problem Statement

[Detailed Problem Statement](https://drive.google.com/drive/folders/1KLyVHyKnnEVi07rY8etdxmpylLhgK7xZ)

## Prerequisites

- Python 3.x
- Django 5.1.3
- SQLite (default database)
- HTML/CSS for frontend

## Folder Structure

```

└── 📁Bynry-OA
    └── 📁accounts
        └── 📁migrations
        └── 📁templates
            └── 📁accounts
                └── login.html
                └── register.html
            └── base.html
        └── __init__.py
        └── admin.py
        └── apps.py
        └── forms.py
        └── models.py
        └── tests.py
        └── urls.py
        └── views.py
    └── 📁Bynry-OA
        └── 📁__pycache__
        └── 📁templates
            └── home.html
        └── __init__.py
        └── asgi.py
        └── settings.py
        └── urls.py
        └── wsgi.py
    └── 📁service_requests
        └── 📁templates
            └── 📁service_requests
                └── request_detail.html
                └── request_list.html
                └── submit_request.html
                └── support_dashboard.html
                └── update_request.html
        └── __init__.py
        └── admin.py
        └── apps.py
        └── forms.py
        └── models.py
        └── tests.py
        └── urls.py
        └── views.py
    └── 📁templates
        └── home.html
    └── db.sqlite3
    └── manage.py
    └── readme.md
```
## Installation and Setup

1. Clone the repository:


`git clone https://github.com/RudradevArya/Bynry-OA.git `
`cd Bynry-OA`

2. Create a virtual environment:

`python -m venv venv source venv/bin/activate # On Windows use venv\Scripts\activate`

3. Install required packages:


`pip install -r requirements.txt`

4. Apply database migrations:


`python manage.py makemigrations`
` python manage.py migrate`

5. Create a superuser:


`python manage.py createsuperuser`

6. Run the development server:


`python manage.py runserver`

7. Access the application at `http://127.0.0.1:8000`


## Usage

### For Customers:
1. Register for an account or log in
2. Submit a new service request from the dashboard
3. View and track existing service requests

### For Support Representatives:
1. Log in with a staff account
2. Access the Support Dashboard
3. View and update service requests

# API Documentation

## Base URL

When running the project locally, all API requests should be made to:

`http://127.0.0.1:8000/`

## Authentication

To authenticate:
1. Log in through the web interface at `http://127.0.0.1:8000/accounts/login/`
2. Once logged in, your browser session will be authenticated for API requests
   (when running `python manage.py createsuperuser` remember the creds)

## Endpoints

### User Authentication

#### Register

- **URL**: `/accounts/register/`
- **Method**: `POST`
- **Data Params**:


```json { "username": "string", "email": "string", "password": "string" }```

- **Success Response**:
  - **Code**: 201
  - **Content**:


```json { "username": "string", "email": "string" }```

#### Login

- **URL**: `/accounts/login/`
- **Method**: `POST`
- **Data Params**:


```json { "username": "string", "password": "string" }```

- **Success Response**:
  - **Code**: 200
  - **Content**:


```json { "message": "Successfully logged in" }```

### Service Requests

#### List User's Service Requests

- **URL**: `/service-requests/list/`
- **Method**: `GET`
- **Success Response**:
  - **Code**: 200
  - **Content**:


```json [ { "id": "integer", "request_type": "string", "description": "string", "status": "string", "created_at": "datetime", "updated_at": "datetime" } ]```

#### Submit Service Request

- **URL**: `/service-requests/submit/`
- **Method**: `POST`
- **Data Params**:


```json { "request_type": "string", "description": "string" }```

- **Success Response**:
  - **Code**: 201
  - **Content**:


```json { "id": "integer", "request_type": "string", "description": "string", "status": "pending", "created_at": "datetime" }```

#### Get Service Request Detail

- **URL**: `/service-requests/detail/<id>/`
- **Method**: `GET`
- **URL Params**: 
  - Required: `id=[integer]`
- **Success Response**:
  - **Code**: 200
  - **Content**:


```json { "id": "integer", "request_type": "string", "description": "string", "status": "string", "created_at": "datetime", "updated_at": "datetime" }```




## Outputs

![Animated gif demo](demo/demo.gif)