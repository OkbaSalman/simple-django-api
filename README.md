# Simple Django API for Hospital Management

Author: Hassan Balleh

## Overview

This project is a simple Django REST API for managing doctors and patients in a hospital context. It provides endpoints to create, read, update, and delete (CRUD) doctor and patient records, with filtering capabilities for availability and insurance status.

## Features

- Manage doctors: add, list, update, and delete doctors
- Manage patients: add, list, update, and delete patients
- Filter doctors by availability
- Filter patients by insurance status
- RESTful API using Django REST Framework

## Project Structure

```
├── Doctor/
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   └── ...
├── Patient/
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   └── ...
├── Hospital/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── ...
├── db.sqlite3
├── manage.py
└── README.md
```

## Models

### Doctor

- `firstName`: CharField (max_length=20)
- `lastName`: CharField (max_length=20)
- `speciality`: CharField (max_length=20)
- `phoneNumber`: CharField (max_length=14)
- `isAvailable`: BooleanField (default=True)

### Patient

- `firstName`: CharField (max_length=20)
- `lastName`: CharField (max_length=20)
- `birthDate`: DateField
- `phoneNumber`: CharField (max_length=14)
- `isInsured`: BooleanField (default=False)

## API Endpoints

All endpoints are prefixed with `/api/`.

### Doctors

- `GET /api/doctors/` — List all doctors
- `POST /api/doctors/` — Create a new doctor
- `GET /api/doctors/{id}/` — Retrieve a doctor by ID
- `PUT /api/doctors/{id}/` — Update a doctor
- `PATCH /api/doctors/{id}/` — Partially update a doctor
- `DELETE /api/doctors/{id}/` — Delete a doctor
- **Filter:** `/api/doctors/?isAvailable=true` — Filter by availability

### Patients

- `GET /api/patients/` — List all patients
- `POST /api/patients/` — Create a new patient
- `GET /api/patients/{id}/` — Retrieve a patient by ID
- `PUT /api/patients/{id}/` — Update a patient
- `PATCH /api/patients/{id}/` — Partially update a patient
- `DELETE /api/patients/{id}/` — Delete a patient
- **Filter:** `/api/patients/?isInsured=true` — Filter by insurance status

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd simple-django-api
   ```
2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   ```bash
   pip install django djangorestframework django-filter
   ```
4. **Apply migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```
6. **Access the API:**
   - API root: [http://localhost:8000/api/](http://localhost:8000/api/)
   - Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

## Example API Usage

### Create a Doctor

```bash
curl -X POST http://localhost:8000/api/doctors/ \
  -H 'Content-Type: application/json' \
  -d '{"firstName": "John", "lastName": "Doe", "speciality": "Cardiology", "phoneNumber": "1234567890", "isAvailable": true}'
```

### List Available Doctors

```bash
curl http://localhost:8000/api/doctors/?isAvailable=true
```

### Create a Patient

```bash
curl -X POST http://localhost:8000/api/patients/ \
  -H 'Content-Type: application/json' \
  -d '{"firstName": "Jane", "lastName": "Smith", "birthDate": "1990-01-01", "phoneNumber": "0987654321", "isInsured": false}'
```

### List Insured Patients

```bash
curl http://localhost:8000/api/patients/?isInsured=true
```

## License

This project is licensed under the MIT License.
