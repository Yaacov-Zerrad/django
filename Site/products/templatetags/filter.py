from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="addcent")
def addcent(value):
    return value + 1000

@register.filter(name="cut")
def cut(value, arg):
    return value.replace(arg, 'jkk')

@register.filter(name="minusc")
@stringfilter
def minusc(value): 
    return value.lower()
    