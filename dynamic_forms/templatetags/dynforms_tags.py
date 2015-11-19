from django import template
from django.conf import settings
import re

numeric_test = re.compile("^\d+$")


register = template.Library()

@register.filter
def getfieldlabel(value, arg):
    """Gets an attribute of an object dynamically from a string name"""
    
    return value[arg].label
    #
    # if hasattr(value, str(arg)):
    #
    #     return getattr(value, arg)
    # elif hasattr(value, 'has_key') and value.has_key(arg):
    #     print(value[arg].__dict__)
    #     return value[arg].label
    # elif numeric_test.match(str(arg)) and len(value) > int(arg):
    #     return value[int(arg)]
    # else:
    #     return settings.TEMPLATE_STRING_IF_INVALID

#register.filter('getattribute', getattribute)

