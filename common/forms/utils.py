from django.forms.utils import ErrorList
from django.utils.html import format_html, format_html_join


class PrettyErrorList(ErrorList):
    def __init__(self, initlist=None, error_class=None):
        super().__init__(initlist)

        if error_class is None:
            self.error_class = 'list-group'
        else:
            self.error_class = 'list-group {}'.format(error_class)

    def as_ul(self):
        if not self.data:
            return ''

        return format_html(
            '<ul class="{}">{}</ul>',
            self.error_class,
            format_html_join('', '<li class="list-group-item list-group-item-danger my-2">{}</li>', ((e,) for e in self))
        )
