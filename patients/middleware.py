import base64
import os


class IHLInfoHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        response['X-IHL-Protection-Header'] = ('This digital infrastructure is protected under humanitarian law. '
                                               'Any unauthorised interference with this digital system may be '
                                               'prosecutable under Geneva Conventions IV Article 18.')
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
