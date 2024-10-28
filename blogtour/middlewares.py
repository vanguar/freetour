# blogtour/middlewares.py

from django.http import HttpResponsePermanentRedirect

class WWWRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if not host.startswith('www.'):
            return HttpResponsePermanentRedirect(f'https://www.{host}{request.get_full_path()}')
        return self.get_response(request)
