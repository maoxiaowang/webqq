from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin

from common.views.mixin import JsonResponseMixin


class ExceptionMiddleware(JsonResponseMixin, MiddlewareMixin):

    def process_request(self, request):
        pass

    def process_response(self, request, response):
        return response

    def process_exception(self, request, e):
        if request.is_ajax():
            return self.json_to_response(result=False, messages=[str(e)])
