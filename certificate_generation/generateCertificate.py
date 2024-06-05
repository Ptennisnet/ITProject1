from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from datetime import datetime, timedelta, timezone

# Private keygen
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Write private key to file
with open("private_key.pem", "wb") as f:
    f.write(
        private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption(),
        )
    )

# Assign attributes
subject = issuer = x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, "AU"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "ACT"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, "Canberra"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, "WCCS"),
    x509.NameAttribute(NameOID.COMMON_NAME, "example.com"),
])

# Build certificate_verification
certificate = (
    x509.CertificateBuilder()
    .subject_name(subject)
    .issuer_name(issuer)
    .public_key(private_key.public_key())
    .serial_number(x509.random_serial_number())
    .not_valid_before(datetime.now(timezone.utc))
    .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))
    .add_extension(
        x509.SubjectAlternativeName([x509.DNSName("example.com")]),
        critical=False,
    )
    .sign(private_key, hashes.SHA256())
)

# Write certificate_verification to file
with open("../certificate_verification/certificate.pem", "wb") as f:
    f.write(certificate.public_bytes(serialization.Encoding.PEM))

print("Certificate and private key generated successfully.")
