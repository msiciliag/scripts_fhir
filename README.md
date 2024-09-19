# scripts_fhir

This directory contains basic scripts for working with FHIR resources. The objective is to demonstrate and learn how to read, extract, edit, sign, and verify basic FHIR resources.

## Pre-requisites

- Python 3.6 or later
- PDM

## Scripts 

### Read, extract and edit FHIR resources
The contents of the `scripts_fhir/src/read_and_edit` directory are as follows:

- `read_from_api.py`: Read a FHIR resource from an API and save it to a json file
- `read_from_json.py`: Read and print a FHIR resource from a json file
- `add_nationality_extesion.py`: Add a nationality extension to a FHIR resource

The intention is to learn how to manage basic FHIR resources using Python.

### Signing and Verifying FHIR Resources
The contents of the `scripts_fhir/src/signature` directory are as follows:

- `README.md`: Instructions for **generating keys and certificates**
- `sign.py`: Sign a FHIR resource
- `verify.py`: Verify a signed FHIR resource
- `convert_jwk.py`: Convert a signed FHIR resource to JWK format

The intention is to learn how to sign and verify FHIR resources using Python for security purposes.

