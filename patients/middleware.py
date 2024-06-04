class IHLHeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        response['X-IHLProtection-Header'] = ('This digital infrastructure is protected under humanitarian law. '
                                              'Any unauthorised interference with this digital system may be '
                                              'prosecutable under Geneva Conventions IV Article 18.')
        return response
