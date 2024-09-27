import json
import base64
from jose import jws, JWTError

with open('provenance.json') as f:
    provenance_resource = json.load(f)

with open('certificate.pem', 'rb') as f:
    public_certificate = f.read()

jws_compact = provenance_resource['signature'][0]['data']

with open('patient.json') as f:
    original_fhir_resource = json.load(f)

with open('public_jwk.json') as f:
  public_jwk = json.load(f)

try:
    decoded_payload = jws.verify(jws_compact, public_jwk, algorithms=['RS256'])
    signed_fhir_resource = json.loads(decoded_payload)

    if original_fhir_resource == signed_fhir_resource:
        print("Signature is valid, and the FHIR resource content matches.")
    else:
      print("Signature is valid, but the FHIR resource content has been modified!")

except JWTError as e:
    print(f"Signature verification failed: {e}") 