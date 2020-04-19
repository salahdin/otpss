from django.core.exceptions import ValidationError
import re


def validate_id(value):
    reg = re.compile('^20[0-9]{7}')
    if not reg.match(value):
        raise ValidationError(u'%s Error: not a student id ' % value)
    return value
