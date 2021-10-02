import datetime
import json

from django.db.models import Model
from django.utils import timezone
from django.forms import model_to_dict


class JsonEncoder(json.JSONEncoder):
    """
    JSONEncoder subclass that knows how to encode date/time, decimal types, and
    UUIDs.
    """
    def default(self, o):
        # See "Date Time String Format" in the ECMA-262 specification.
        if isinstance(o, datetime.datetime):
            return timezone.localtime(o).strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, Model):
            return model_to_dict(o)
        else:
            return super().default(o)
