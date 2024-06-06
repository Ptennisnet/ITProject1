import base64
import os


class IHLInfoHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        directory = os.path.dirname(__file__)
        plaintext_path = os.path.join(directory[:-8], 'IHLCertificate/plaintext_header.txt')
        with open(plaintext_path, 'r') as plain_file:
            header_content = plain_file.read()

        response['X-IHL-Protection-Header'] = header_content
        return response


class IHLCertificateHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        directory = os.path.dirname(__file__)
        certificate_path = os.path.join(directory[:-8], 'IHLCertificate/certificate.pem')
        with open(certificate_path, 'rb') as cert_file:
            certificate = cert_file.read()
        encoded_cert = base64.b64encode(certificate).decode('utf-8')

        response['X-IHL-Certificate-Header'] = encoded_cert
        return response
