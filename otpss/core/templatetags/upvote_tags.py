from django import template

register = template.Library()

@register.simple_tag
def has_voted(number):
    return True



