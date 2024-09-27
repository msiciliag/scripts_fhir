''' This script demonstrates how to sign a FHIR resource using a private key and create a Provenance resource with the signature. '''
import json
import base64
from jose import jws
from datetime import datetime, timezone

with open('patient.json', encoding='utf-8') as f:
    fhir_resource = json.load(f)

with open('private_key.pem', 'rb') as f:
    private_key = f.read()

jws_compact = jws.sign(
    fhir_resource,
    private_key,
    algorithm='RS256',
)

now_utc = datetime.now(timezone.utc)
patient_id = fhir_resource['id']

provenance_resource = {
    "resourceType": "Provenance",
    "target": [
        {"reference": "Patient/" + patient_id}
    ],
    "recorded": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
    "activity": {
        "coding": [
            {"system": "http://terminology.hl7.org/CodeSystem/v3-DocumentCompletion", "code": "LA"}
        ]
    },
    "signature": [
        {
            "type": [
                {"system": "urn:iso-astm:E1762-95:2013", "code": "1.2.840.10065.1.12.1.1"}
            ],
            "when": now_utc.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "sigFormat": "application/jose",
            "data": jws_compact
        }
    ]
}

# Save the Provenance resource to a file

with open('provenance.json', 'w', encoding='utf-8') as f:
    json.dump(provenance_resource, f, ensure_ascii=False, indent=4)
