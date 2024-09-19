from fhirclient import client
from fhirclient.models.patient import Patient
import json

settings = {
    'app_id': 'my_web_app',
    'api_base': 'https://fhirsandbox.healthit.gov/open/r4/fhir'
}
smart = client.FHIRClient(settings=settings)

patient = Patient.read('123d41e1-0f71-4e9f-8eb2-d1b1330201a6', smart.server)
print(patient.birthDate.isostring)
print(smart.human_name(patient.name[0]))

with open('patient-api.json', 'w') as f:
    json.dump(patient.as_json(), f, indent=4) 