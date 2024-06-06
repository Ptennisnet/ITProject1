import base64


def signature_to_pem(encoded_cert):
    decoded_cert_bytes = base64.b64decode(encoded_cert)
    decoded_cert = decoded_cert_bytes.decode('utf-8')
    with open('untrusted_certificate.pem', 'w') as file:
        file.write(decoded_cert)


with open('input_file.txt', 'r') as input_file:
    cert_data = input_file.read()

signature_to_pem(cert_data)
