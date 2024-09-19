from fhirclient import client
from fhirclient.models.patient import Patient
from fhirclient.models.fhirabstractbase import FHIRValidationError
import json
import os

def print_patient_from_json():
    patient = read_json_file()

    print(f"Patient Name: {patient.name[0].given[0]} {patient.name[0].family}")
    print(f"Patient Birth Date: {patient.birthDate.isostring}")

def read_json_file():
    print("Files in the directory:")
    file_names = []
    for i, file in enumerate(os.listdir()):
        if not file.endswith(".json"):
            continue
        print(f"{i}. {file}")
        file_names.append(f"{file}")

    file = input("Enter the number of the file you want to read: ")
    file_name = file_names[int(file)]

    try:
        with open(file_name, 'r') as f:
            patient_data = json.load(f)
    except FileNotFoundError:
        print("File not found. Exiting...")
        exit()

    try:
        patient = Patient(patient_data)
        return patient
    except FHIRValidationError as e:
        print("Error: ", e)
        return None

# Para pruebas locales
if __name__ == "__main__":
    print_patient_from_json()