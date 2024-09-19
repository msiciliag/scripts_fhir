# Signing and Verifying FHIR Resources
This directory contains scripts for signing and verifying FHIR resources.

## Usage

### Key generation:
Run the following commands to generate a private key, a public key, and a certificate:
```bash
openssl req -x509 -newkey rsa:4096 -nodes -keyout private_key.pem -out certificate.pem -days 365 -subj "/C=US/ST=California/L=San Francisco/O=MyOrg/CN=JohnDoe"
openssl x509 -in certificate.pem -pubkey -noout > public_key.pem
```

### Signing:
Run `sign.py`

### Verifying:
Run `verify.py`
Try altering the signed resource and verify again. You will see that the verification tells you that the resource has been tampered.