from django.core.exceptions import ValidationError
import re


def validate_id(value):
    reg = re.compile('^20[0-9]{7}')
    if not reg.match(str(value)):
        raise ValidationError(u'%s Error: not a student id ' % str(value))
    return value
