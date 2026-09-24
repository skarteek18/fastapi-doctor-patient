from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, Field
from typing import List


app = FastAPI(
    title="Doctor & Patient Management API",
    description="Simple REST API using FastAPI",
    version="1.0.0"
)


# -----------------------------
# Pydantic Models
# -----------------------------

class Doctor(BaseModel):
    name: str
    specialization: str
    email: EmailStr
    is_active: bool = True


class DoctorResponse(Doctor):
    id: int


class Patient(BaseModel):
    name: str
    age: int = Field(..., gt=0)
    phone: str


class PatientResponse(Patient):
    id: int


# -----------------------------
# In-memory storage
# -----------------------------

doctors: List[DoctorResponse] = []
patients: List[PatientResponse] = []

doctor_id_counter = 1
patient_id_counter = 1


# -----------------------------
# Doctor APIs
# -----------------------------

@app.post("/doctors", response_model=DoctorResponse, status_code=201)
def create_doctor(doctor: Doctor):
    global doctor_id_counter

    # Check duplicate email
    for existing_doctor in doctors:
        if existing_doctor.email == doctor.email:
            raise HTTPException(
                status_code=400,
                detail="Doctor with this email already exists"
            )

    new_doctor = DoctorResponse(
        id=doctor_id_counter,
        **doctor.model_dump()
    )

    doctors.append(new_doctor)
    doctor_id_counter += 1

    return new_doctor


@app.get("/doctors", response_model=List[DoctorResponse])
def get_doctors():
    return doctors


@app.get("/doctors/{doctor_id}", response_model=DoctorResponse)
def get_doctor(doctor_id: int):
    for doctor in doctors:
        if doctor.id == doctor_id:
            return doctor

    raise HTTPException(
        status_code=404,
        detail="Doctor not found"
    )


# -----------------------------
# Patient APIs
# -----------------------------

@app.post("/patients", response_model=PatientResponse, status_code=201)
def create_patient(patient: Patient):
    global patient_id_counter

    new_patient = PatientResponse(
        id=patient_id_counter,
        **patient.model_dump()
    )

    patients.append(new_patient)
    patient_id_counter += 1

    return new_patient


@app.get("/patients", response_model=List[PatientResponse])
def get_patients():
    return patients
