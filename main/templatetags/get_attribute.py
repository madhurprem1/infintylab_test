from django import template

register = template.Library()


@register.filter(name='get_attribute')
def get_attribute(value, key):
    return getattr(value, key)