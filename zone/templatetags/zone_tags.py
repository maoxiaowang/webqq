from django import template

from common.utils.json import JsonEncoder

register = template.Library()


@register.filter
def custom_page_range(page_range, cur_page):
    num_pages = len(page_range)
    pagination_number = 7
    if pagination_number % 2:
        # odd
        before = after = int((pagination_number - 1) / 2)
    else:
        # even
        before = int(pagination_number / 2)
        after = pagination_number - before - 1

    if cur_page - 1 < before:
        start = 0
        end = pagination_number
    elif num_pages - cur_page < after:
        start = num_pages - pagination_number
        end = num_pages
    else:
        start = cur_page - before - 1
        end = start + pagination_number
    start = start if start >= 0 else 0
    return page_range[start: end]


@register.filter
def django_page_range(paginator, cur_page):
    return paginator.get_elided_page_range(cur_page)


@register.filter
def custom_datetime(value):
    return JsonEncoder().default(value)
