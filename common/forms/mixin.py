from common.views.mixin import JsonResponseMixin


class JsonFormMixin(JsonResponseMixin):

    def form_valid(self, form):
        self.object = form.save()
        return self.json_to_response(data=self.object)

    def form_invalid(self, form):
        messages = [' '.join(e) for f, e in form.errors.items()]
        return self.json_to_response(result=False, messages=messages)
