import copy

from django.http import JsonResponse
from django.views.generic.edit import DeletionMixin as _DeletionMixin

from common.utils.json import JsonEncoder


class JsonResponseMixin:

    def json_to_response(self, result: bool = True, data=None, messages: list = None,
                         **json_kwargs):

        if messages is None:
            messages = []
        if not isinstance(messages, list):
            messages = [messages]
        response_data = {
            'result': result,
            'data': data,
            'messages': messages
        }
        return JsonResponse(
            data=response_data,
            encoder=JsonEncoder,
            **json_kwargs
        )


class DeletionMixin(JsonResponseMixin, _DeletionMixin):
    json = False

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        if self.json:
            self.object = self.get_object()
            obj = copy.deepcopy(self.object)
            self.object.delete()
            return self.json_to_response(data=obj)
        else:
            return super().delete(request, *args, **kwargs)
