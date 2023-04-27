import jalali_date
from django import template
register = template.Library()
from jalali_date import date2jalali
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')
@register.filter(name='lower')
def lower(value): # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()
@register.filter(name='show_jalai_date')
def show_jalali_date(value):
    return date2jalali(value)


register.filter('cut', cut)
