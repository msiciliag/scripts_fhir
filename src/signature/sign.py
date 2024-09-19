''' This script demonstrates how to sign a FHIR resource using a private key and create a Provenance resource with the signature. '''
import json
import base64
from jose import jws

# Load the FHIR resource
with open('patient.json', encoding='utf-8') as f:
    fhir_resource = json.load(f)

# Load the private key
with open('private_key.pem', 'rb') as f:
    private_key = f.read()

jws_compact = jws.sign(
    fhir_resource,
    private_key,
    algorithm='RS256',
    headers={'kid': 'my_key_id'}  # Optional: Key ID for identifying the signing key
)

# Create the Provenance resource
provenance_resource = {
    "resourceType": "Provenance",
    "target": [
        {"reference": "Patient/example"}
    ],
    "recorded": "2024-11-16T12:00:00Z",  # Use current timestamp
    "activity": {
        "coding": [
            {"system": "http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion", "code": "LA"}
        ]
    },
    "agent": [
        {
            "type": {
                "coding": [
                    {"system": "http://terminology.hl7.org/CodeSystem/provenance-participant-type", "code": "author"}
                ]
            },
            "who": {
                "reference": "Practitioner/your_practitioner_id"  #Replace with your practitioner ID
            }
        }
    ],
    "signature": [
        {
            "type": [
                {"system": "urn:iso-astm:E1762-95:2013", "code": "1.2.840.10065.1.12.1.1"}
            ],
            "when": "2024-11-16T12:00:00Z",  # Use the same timestamp
            "who": {
                "reference": "Practitioner/your_practitioner_id"  #Replace with your practitioner ID
            },
            "sigFormat": "application/jose",
            "data": jws_compact
        }
    ]
}

# Save the Provenance resource to a file

with open('provenance.json', 'w', encoding='utf-8') as f:
    json.dump(provenance_resource, f, ensure_ascii=False, indent=4)
