from cryptography import x509
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from datetime import datetime, timezone

# Load certificate
with open("untrusted_certificate.pem", "rb") as f:
    certificate = x509.load_pem_x509_certificate(f.read())

# Load public key from file
public_key = certificate.public_key()

# Verify signature
try:
    public_key.verify(
        certificate.signature,
        certificate.tbs_certificate_bytes,
        padding.PKCS1v15(),
        certificate.signature_hash_algorithm,
    )
    print("Certificate signature is valid.")
except Exception as e:
    print(f"Certificate signature is invalid: {e}")

# Check validity period
current_time = datetime.now(timezone.utc)
if certificate.not_valid_before_utc <= current_time <= certificate.not_valid_after_utc:
    print("Certificate is within its validity period.")
else:
    print("Certificate is not within its validity period.")
