import json
from django.utils.safestring import mark_safe
from django.template import Library
from django import template

register = template.Library()


@register.filter
def pretty_json(value):
    return json.dumps(value, indent=4)
@register.filter(is_safe=True)
def js(obj):
    return mark_safe(json.dumps(obj))