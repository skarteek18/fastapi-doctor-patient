FastAPI Doctor & Patient Management API

A simple REST API built using Python, FastAPI and Pydantic to manage doctors and patients.

Technologies Used

- Python 3.9+
- FastAPI
- Pydantic
- Uvicorn
- In-memory storage

Project Structure

fastapi-doctor-patient-api/
│
├── main.py
├── requirements.txt
└── README.md

Installation

1. Clone the repository

git clone <YOUR_GITHUB_REPOSITORY_URL>
cd fastapi-doctor-patient-api

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

4. Install dependencies

pip install -r requirements.txt

Run the Application

Start the FastAPI server using:

uvicorn main:app --reload

The application will be available at:

http://127.0.0.1:8000

API Documentation

FastAPI provides interactive API documentation at:

http://127.0.0.1:8000/docs

You can use Swagger UI to test all API endpoints.

API Endpoints

Doctor APIs

Method| Endpoint| Description
POST| "/doctors"| Create a doctor
GET| "/doctors"| List all doctors
GET| "/doctors/{doctor_id}"| Get doctor by ID

Patient APIs

Method| Endpoint| Description
POST| "/patients"| Create a patient
GET| "/patients"| List all patients

Validation

The API includes the following validations:

- Doctor email must be valid.
- Patient age must be greater than 0.
- Doctor "is_active" defaults to "true".
- Duplicate doctor emails are not allowed.
- HTTP 404 is returned when a doctor is not found.
- HTTP 400 is returned for duplicate doctor emails.

Example Doctor Request

{
    "name": "Dr. Ravi Kumar",
    "specialization": "Cardiology",
    "email": "ravi@gmail.com"
}

Example Patient Request

{
    "name": "Kiran",
    "age": 25,
    "phone": "9876543210"
}

Author

Karteek
