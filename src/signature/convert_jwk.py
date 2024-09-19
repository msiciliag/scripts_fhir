import json
from jwcrypto import jwk

with open('public_key.pem', 'rb') as f:
    key = jwk.JWK.from_pem(f.read())

public_jwk = key.export_public()
with open('public_jwk.json', 'w') as f:
    json.dump(json.loads(public_jwk), f, indent=4)