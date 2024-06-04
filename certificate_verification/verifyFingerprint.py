from cryptography import x509
from cryptography.hazmat.primitives import hashes


# Load certificates
with open("untrusted_certificate.pem", "rb") as f:
    untrusted_certificate = x509.load_pem_x509_certificate(f.read())

with open("certificate.pem", "rb") as f:
    trusted_certificate = x509.load_pem_x509_certificate(f.read())

expected_fingerprint = trusted_certificate.fingerprint(hashes.SHA256()).hex()
actual_fingerprint = untrusted_certificate.fingerprint(hashes.SHA256()).hex()

# Test fingerprint
if actual_fingerprint == expected_fingerprint:
    print("Certificate fingerprint matches.")
else:
    print("Certificate fingerprint does not match.")
