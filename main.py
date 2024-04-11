import json

from fastapi import FastAPI

from modules import Patient


with open("patients.json", "r") as f:
    patient_list = json.load(f)

# Use the first name as the unique identifier. For example, in the PUT route, you'd have something like this: "/patients/{first_name}"

app = FastAPI()

@app.get("/patients")
def get_patients()-> list:
    return patient_list

@app.post("/patients")
def create_patient(patient: Patient):
    patient_list.append(patient)
    return patient

@app.put("/patients/{first_name}")
def update_patient(first_name, patient: Patient):
    for p in patient_list:
        if p["first_name"] == first_name:
            p.update(patient.model_dump())
            return p
        
@app.delete("/patients/{first_name}")
def delete_patient(first_name):
    for p in patient_list:
        if p["first_name"] == first_name:
            patient_list.remove(p)
            return p