from django import template
from django.utils.http import urlencode
from goods.models import *


register = template.Library()


@register.simple_tag()
def tag_categories():
    return Categories.objects.all()


@register.simple_tag(takes_context=True)
def chang_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)