from fhirclient import client
from fhirclient.models.patient import Patient
from fhirclient.models.extension import Extension
from fhirclient.models.codeableconcept import CodeableConcept
from fhirclient.models.coding import Coding
import json

#Read the patient data from a file
with open('patient.json', 'r') as f:
    patient_data = json.load(f)

patient = Patient(patient_data)

nationality_extension_url = "https://hl7.fr/ig/fhir/core/StructureDefinition/fr-core-patient-nationality"

nationality_codeableconcept = CodeableConcept()
nationality_coding = Coding()
nationality_coding.system = "http://terminology.hl7.org/CodeSystem/v3-Nationality"
nationality_coding.code = "CA" 
nationality_coding.display = "Canadian"
nationality_codeableconcept.coding = [nationality_coding]

nationality_extension = Extension()
nationality_extension.url = nationality_extension_url
nationality_extension.valueCodeableConcept = nationality_codeableconcept

if patient.extension is None:
    patient.extension = []
patient.extension.append(nationality_extension)

if not patient.name:
    patient.name = [{}]
patient.name[0].family = "Canadian Patient"

print("National Codeable Concept Display: ", patient.extension[0].valueCodeableConcept.coding[0].display)

with open('patient-nationality.json', 'w', encoding='utf-8') as f:
    json.dump(patient.as_json(), f, indent=4)
